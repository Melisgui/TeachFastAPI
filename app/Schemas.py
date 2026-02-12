from datetime import date
from enum import Enum
from pydantic import BaseModel


class Lessons(str, Enum):
    physics = "Physics"
    mathematics = "Mathematics"
    english = "English"
    russian = "Russian"
    geography = "Geography"
    literature = "Literature"

class EducationLevel(str, Enum):
    School = "School"
    College = "College"
    University = "University"

class UserBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    date_of_birth: date
    education_level: EducationLevel

class UserCreate(UserBase):
    password: str  # ← только здесь

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# --- Схемы для Teacher ---
class TeacherBase(UserBase):
    teach_lesson: Lessons
    teacher_experience: int
    experience_description: str

class TeacherCreate(TeacherBase):
    password: str

class TeacherResponse(TeacherBase):
    id: int

    class Config:
        from_attributes = True

# --- Схемы для Student ---
"""class StudentBase(UserBase):
    desired_score: int
    education_class: int

class StudentCreate(StudentCreate):
    password: str

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True"""