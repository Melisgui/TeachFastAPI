from datetime import date
import enum
from pydoc import describe

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from ..database import Base


class EducationLevel(enum.Enum):
    School = "School"
    College = "College"
    University = "University"


class Lessons(enum.Enum):
    physics = "Physics"
    mathematics = "Mathematics"
    english = "English"
    russian = "Russian"
    geography = "Geography"
    literature = "Literature"


class User(Base):
    """
    Родительская таблица сущности пользователя содержащая основную, общую информацию
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, index=True)
    date_of_birth = Column(Date)
    hash_password = Column(String)
    education_level = Column(Enum(EducationLevel), index=True)


class Teacher(Base):
    """
    Дочерняя таблица от users, содержит уникальные данные преподавателя
    """
    __tablename__ = "teacher"
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    teach_lesson = Column(Enum(Lessons), index=True)
    teacher_experience = Column(Integer)
    experience_description = Column(String)
    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }


class Student(Base):
    """
    Дочерняя таблица от users, содержит уникальные данные ученика
    - education_class - номер класса(1 - 11) или же курса (1 - 5)
    """
    __tablename__ = "student"
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    desired_score = Column(Integer)
    education_class = Column(Integer)
    __mapper_args__ = {
        "polymorphic_identity": "student",
    }
