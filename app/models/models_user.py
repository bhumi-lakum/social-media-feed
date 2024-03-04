from odmantic import Field, Model
from pydantic import EmailStr
from datetime import datetime
from typing import Optional


class User(Model):
    """
    Container for a single user record.
    """
    username: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    model_config = {
        "collection": "users"
    }
