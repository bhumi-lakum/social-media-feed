from typing import Optional

from odmantic import Field
from odmantic import Field, Model

from datetime import datetime



class Posts(Model):
    """
    Container for a single post record.
    """

    title: str = Field(...)
    content: str = Field(...)
    published: bool = Field(...)
    author_id: str = Field(...)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)