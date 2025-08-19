from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

# Base is the declarative base class for SQLAlchemy models.
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    # Ensure email uniqueness for user identification. Remove `unique=True` if not required.
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    posts = relationship(
        "Post", 
        back_populates="user", 
        cascade="all, delete-orphan",
        passive_deletes=True
        )
    # nickname = Column(String(32), nullable=False)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False
        )
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="posts")