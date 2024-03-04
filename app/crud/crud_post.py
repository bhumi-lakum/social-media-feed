"""
    CRUD POST FILE
"""

import logging
from app.crud.crud_base import CRUDBase
from app.models.models_post import Posts
from app.schemas.schemas_post import PostCreate, PostUpdate

# get root logger
logger = logging.getLogger(__name__)


class CRUDPost(CRUDBase[Posts, PostCreate, PostUpdate]):
    """
    CRUD CLASS - POST
    """


crud_post = CRUDPost(Posts)
