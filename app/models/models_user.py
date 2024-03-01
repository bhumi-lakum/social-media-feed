from typing import Optional

from odmantic import Field, Model, ObjectId
from pydantic import EmailStr

from app.models.models_base import CustomBaseModel


class User(Model):
    """
    Container for a single user record.
    """
    user_name:str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
