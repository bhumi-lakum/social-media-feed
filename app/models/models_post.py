from typing import Optional
from odmantic import Field, Model, ObjectId
from datetime import datetime

class Posts(Model):
    """
    Container for a single post record.
    """

    title: str = Field(...)
    content: str = Field(...)
    published: bool = Field(...)
    author_id: ObjectId = Field(...)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    model_config = {
        "collection": "posts"
    }
