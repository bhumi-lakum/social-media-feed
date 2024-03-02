from datetime import datetime
from typing import Optional

from odmantic import Field, Model


class CustomBaseModel(Model):
    """
    Custom base model for all other models to inherit from.
    """
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
