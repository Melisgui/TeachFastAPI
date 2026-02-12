import enum
from enum import Enum

class EducationLevel(str, enum.Enum):
    School = "School"
    College = "College"
    University = "University"

class Lesson(str, enum.Enum):
    physics = "Physics"
    mathematics = "Mathematics"
    english = "English"
    russian = "Russian"
    geography = "Geography"
    literature = "Literature"