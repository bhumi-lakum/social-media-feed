"""
    CRUD POST FILE
"""

import logging
from typing import Optional
from app.crud.crud_base import CRUDBase
from app.models.models_post import Posts
from app.schemas.schemas_post import PostCreate, PostUpdate

# get root logger
logger = logging.getLogger(__name__)


class CRUDPost(CRUDBase[Posts, PostCreate, PostUpdate]):
    """
    CRUD CLASS - POST
    """
    def get_personised_posts(self, author_id: str, skip: int, limit: int):
        """
        Method to get personised posts
        """
        offset = {"skip": skip, "limit": limit}
        return self.engine.find(self.model, self.model.author_id == author_id, **offset)


crud_post = CRUDPost(Posts)
