from typing import Optional

from odmantic import Field, ObjectId
from app.models.models_base import CustomBaseModel


class Follows(CustomBaseModel):
    """
    Container for a single follow record.
    """

    follower_id: ObjectId = Field(...)
    followed_id: ObjectId = Field(...)

    class Config:

