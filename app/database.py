from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL для подключения к PostgreSQL
DATABASE_URL = "postgresql://postgres:1234@localhost/project"

# Создаём движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаём фабрику сессий для взаимодействия с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Подключение
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
