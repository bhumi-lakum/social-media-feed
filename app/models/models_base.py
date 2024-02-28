from datetime import datetime
from typing import Optional

from odmantic import Field, Model, ObjectId


def current_timestamp():
    return datetime.now().replace(microsecond=0)


class CustomBaseModel(Model):
    """
    Custom base model for all other models to inherit from.
    """

    id: Optional[ObjectId] = Field(primary_field=True, default=None)
    created_at: Optional[str] = Field(default_factory=current_timestamp)
    updated_at: Optional[str] = Field(default_factory=current_timestamp)
