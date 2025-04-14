from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.domain.models import Base
from app.services.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Вызывается при старте
def init_db():
    Base.metadata.create_all(bind=engine)

# Зависимость для роутов
def get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
