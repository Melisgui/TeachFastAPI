from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from ..database import Base
from ..Enum import Lesson, EducationLevel


"""
Здесь хранятся все pydantic модели
"""

class User(Base):
    """
    Родительская таблица сущности пользователя содержащая основную, общую информацию
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    middle_name = Column(String,nullable=False)
    date_of_birth = Column(Date,nullable=False)
    hash_password = Column(String,nullable=False)
    education_level = Column(Enum(EducationLevel),nullable=False)


class Teacher(Base):
    """
    Дочерняя таблица от users, содержит уникальные данные преподавателя
    """
    __tablename__ = "teacher"
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    teach_lesson = Column(Enum(Lesson), index=True)
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