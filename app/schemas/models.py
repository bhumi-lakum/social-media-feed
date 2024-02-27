from fastapi.responses import Response
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """
    Container for a single student record.
    """

    # The primary key for the StudentModel, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: str = Field(alias="_id", default=None)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "password": "secretpassword",
            }
        }


class Posts(User):
    """
    Container for a single post record.
    """

    title: str = Field(...)
    content: str = Field(...)
    published: Optional[bool] = Field(...)
    author_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "My First Post",
                "content": "This is the content of my first post",
                "published": True,
                "author_id": "5f0b3f3e0ff1a4e3d0e4e4d5",
            }
        }


class Follows(User):
    """
    Container for a single follow record.
    """

    follower_id: str = Field(...)
    followed_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "follower_id": "5f0b3f3e0ff1a4e3d0e4e4d5",
                "followed_id": "5f0b3f3e0ff1a4e3d0e4e4d6",
            }
        }


