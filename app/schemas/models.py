from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from bson import ObjectId


class CustomBaseModel(BaseModel):
    """
    Custom base model for all other models to inherit from.
    """

    created_at: Optional[str] = Field(alias="created_at", default=datetime.now())
    updated_at: Optional[str] = Field(alias="updated_at", default=datetime.now())

    class Config:
        orm_mode = True


class User(CustomBaseModel):
    """
    Container for a single student record.
    """

    id: Optional[ObjectId] = Field(alias="_id", default=None)
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


class Posts(CustomBaseModel):
    """
    Container for a single post record.
    """

    id: Optional[ObjectId] = Field(alias="_id", default=None)
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


class Follows(CustomBaseModel):
    """
    Container for a single follow record.
    """

    id: Optional[ObjectId] = Field(alias="_id", default=None)
    follower_id: str = Field(...)
    followed_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "follower_id": "5f0b3f3e0ff1a4e3d0e4e4d5",
                "followed_id": "5f0b3f3e0ff1a4e3d0e4e4d6",
            }
        }


