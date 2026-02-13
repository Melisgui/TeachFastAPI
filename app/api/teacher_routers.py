from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import logging

from ..Schemas import TeacherResponse, TeacherCreate
from ..database import get_db
from .models import Teacher

from .user_routers import read_user

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/teacher", tags=["teacher"])

@router.post("/create",response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    try:
        db_teacher = Teacher(
            id = db.query()
        )