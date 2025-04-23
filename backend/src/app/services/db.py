from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..domain.models import Base
from .config import settings

DATABASE_URL = settings.postgres_url

engine = create_engine(DATABASE_URL)

# engine = create_engine(conn_string, connect_args=conn_args,pool_pre_ping=True,pool_recycle=300)

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
