from typing import Optional
from datetime import datetime
from odmantic import ObjectId
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool


class PostCreate(PostBase):
    author_id: ObjectId


class PostUpdate(BaseModel):
    title: str
    content: str


class PostView(PostBase):
    id: ObjectId
    author_id: ObjectId
    created_at: datetime
    updated_at: datetime

# class PostInDBBase(PostBase):
#     id: Optional[ObjectId] = None
#     author_id: Optional[ObjectId] = None


# class FollowBase(BaseModel):
#     follower_id: ObjectId
#     followed_id: ObjectId


# class FollowCreate(FollowBase):
#     follower_id: ObjectId
#     followed_id: ObjectId


# class FollowInDBBase(FollowBase):
#     id: Optional[ObjectId] = None
#     follower_id: Optional[ObjectId] = None
#     followed_id: Optional[ObjectId] = None
