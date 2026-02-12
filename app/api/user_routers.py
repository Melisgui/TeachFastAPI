from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import EducationLevel
from ..Schemas import UserCreate
from ..database import get_db
from ..crud.userCrud import get_user,create_user_crud
from datetime import date
from ..crud.userCrud import create_user_crud


router = APIRouter(prefix="/user",tags=['Users'])


@router.post("/create")
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_crud(db, user)


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user