from litestar import post, Request, Response
from litestar.exceptions import HTTPException
from litestar.di import Provide
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from ..services.db import get_db_session
from ..services import auth_service as auth

class RegisterDTO(BaseModel):
    email: EmailStr
    password: str

class LoginDTO(BaseModel):
    email: EmailStr
    password: str

@post("/register", dependencies={"db": Provide(get_db_session)})
async def register(data: RegisterDTO, db: Session) -> dict:
    if auth.get_user_by_email(data.email, db):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = auth.create_user(data.email, data.password, db)
    return {"msg": "registered", "user_id": user.id}

@post("/login", dependencies={"db": Provide(get_db_session)})
async def login(data: LoginDTO, db: Session) -> dict:
    user = auth.get_user_by_email(data.email, db)
    if not user or not auth.verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}
