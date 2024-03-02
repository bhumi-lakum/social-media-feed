from typing import Optional

from odmantic import ObjectId
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserLogin(UserBase):
    password: str


class UserCreate(UserBase):
    id: Optional[ObjectId] = None
    user_name: str
    first_name: str
    last_name: str
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserView(BaseModel):
    id: ObjectId
    user_name: str
    first_name: str
    last_name: str
