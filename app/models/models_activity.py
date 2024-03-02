from odmantic import Field, Model, ObjectId
from datetime import datetime
from typing import Optional


class FollowUser(Model):
    """
    Container for a single user record.
    """
    follower_id: ObjectId = Field(...)
    followed_id: ObjectId = Field(...)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    model_config = {
        "collection": "followers"
    }
