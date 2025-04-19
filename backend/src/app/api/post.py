from typing import Annotated
from litestar import Controller, post, get, delete, Request, Response
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_201_CREATED, HTTP_200_OK
from litestar.di import Provide
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.domain.models import Post as PostModel

from app.services.db import get_db_session


class PostDTO(BaseModel):
    title: str 
    content: str 
    created_at: datetime 
    user_id: int 

    class Config:
            from_attributes = True 

class PostController(Controller):
    path = "/posts"
    tags = ["posts"]

    @post("/create", status_code=HTTP_201_CREATED, dependencies={"db": Provide(get_db_session)})
    async def create_post(self, data: PostDTO, db: Session) -> dict:
        """
        Create a new post.
        """
        try:
            if not data.title or not data.content:
                raise HTTPException(status_code=400, detail="Title and content are required")
            
            new_post = PostModel(**data.model_dump())
            db.add(new_post)
            db.commit()
            db.refresh(new_post)

            return {"msg": "Post created", "post": PostDTO.model_validate(new_post)}
        
        except HTTPException as http_exc:
            # Log the HTTP exception for debugging purposes
            print(f"HTTPException occurred: {http_exc.detail}")
            raise http_exc
        except Exception as exc:
            # Log the unexpected exception for debugging purposes
            print(f"Unexpected error: {exc}")
            db.rollback()
            raise HTTPException(status_code=500, detail="An unexpected error occurred") from exc


    @get("/all", status_code=HTTP_200_OK, dependencies={"db": Provide(get_db_session)})
    async def get_all_posts(self, db: Session) -> list[PostModel]:
        try:
            posts = db.query(PostModel).all()
            return [PostDTO.model_validate(post) for post in posts]
        except Exception as exc:
            # Log the unexpected exception for debugging purposes
            print(f"Unexpected error while fetching posts: {exc}")
            raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching posts") from exc