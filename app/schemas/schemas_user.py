from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class User(BaseModel):
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class ShowUser(User):
    id: int

    class Config:
        orm_mode = True


class ShowUserFew(BaseModel):
    id: int
    email: str


class ShowUserList(BaseModel):
    users: List[ShowUser]
    skip: int
    limit: int


class ShowFollowers(BaseModel):
    followers: List[ShowUserFew]
    skip: int
    limit: int


class ShowFollowing(BaseModel):
    following: List[ShowUserFew]
    skip: int
    limit: int


class ShowUserPosts(BaseModel):
    id: int
    email: str
    posts: List[Dict[str, Any]]

    class Config:
        orm_mode = True
