from typing import Optional

from odmantic import Field

from app.models.models_base import CustomBaseModel


class Posts(CustomBaseModel):
    """
    Container for a single post record.
    """

    title: str = Field(...)
    content: str = Field(...)
    published: Optional[bool] = Field(...)
    author_id: str = Field(...)
