from typing import Optional

from odmantic import Field

from app.models.models_base import CustomBaseModel


class Follows(CustomBaseModel):
    """
    Container for a single follow record.
    """

    follower_id: str = Field(...)
    followed_id: str = Field(...)
