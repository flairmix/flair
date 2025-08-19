from typing import Annotated
from litestar import Controller, post, get, delete, Request, Response
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_201_CREATED, HTTP_200_OK
from litestar.di import Provide
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from ..domain.models import Post as PostModel

from ..services.db import get_db_session

from ..engineering_lib.water_consumption_sp30 import calculate_NPhv

class PostDTO(BaseModel):
    title: str 
    content: str 
    created_at: datetime 
    user_id: int 

    class Config:
            from_attributes = True 

class WaterController(Controller):
    path = "/water"
    tags = ["water"]

    @get("/calculate_NPhv", status_code=HTTP_200_OK)
    async def get_calculate_NPhv(self) -> float:
        try:
            return 123
        except Exception as exc:
            # Log the unexpected exception for debugging purposes
            print(f"Unexpected error while fetching posts: {exc}")
            raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching posts") from exc

    # @get("/all", status_code=HTTP_200_OK, dependencies={"db": Provide(get_db_session)})
    # async def get_all_posts(self, db: Session) -> list[PostModel]:
    #     try:
    #         posts = db.query(PostModel).all()
    #         return [PostDTO.model_validate(post) for post in posts]
    #     except Exception as exc:
    #         # Log the unexpected exception for debugging purposes
    #         print(f"Unexpected error while fetching posts: {exc}")
    #         raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching posts") from exc