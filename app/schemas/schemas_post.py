from typing import Optional

from odmantic import ObjectId
from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool


class PostCreate(PostBase):
    title: str
    content: str
    author_id: ObjectId

class PostUpdate(PostBase):
    title: str
    content: str

class PostView(PostBase):
    id: ObjectId
    author_id: ObjectId
    created_at: Optional[datetime]
    updated_at: Optional[datetime] 

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
