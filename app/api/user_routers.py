from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status
from sqlalchemy.future import select
import logging

from ..Schemas import UserCreate
from ..database import get_db
from ..Schemas import UserResponse
from .models import User


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/user",tags=['Users'])


@router.post("/create", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = User(**user.dict())
    logger.info(f"📥 Создание пользователя: {user.email},{user.hash_password},{user.first_name}")
    #logger.debug(f"📥 Полные данные: {user.dict()}")
    db.add(user)
    db.commit()
    return user


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    res = db.execute(select(User).where(User.id == user_id))
    user = res.scalar()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user