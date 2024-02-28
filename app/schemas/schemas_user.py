from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    username: str
    password: str


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserInDBBase(UserBase):
    id: Optional[ObjectId] = None
    email: EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = False


class PostCreate(PostBase):
    title: str
    content: str
    author_id: ObjectId


class PostInDBBase(PostBase):
    id: Optional[ObjectId] = None
    author_id: Optional[ObjectId] = None


class FollowBase(BaseModel):
    follower_id: ObjectId
    followed_id: ObjectId


class FollowCreate(FollowBase):
    follower_id: ObjectId
    followed_id: ObjectId


class FollowInDBBase(FollowBase):
    id: Optional[ObjectId] = None
    follower_id: Optional[ObjectId] = None
    followed_id: Optional[ObjectId] = None
