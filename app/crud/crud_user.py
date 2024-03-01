"""
    CRUD USER FILE
"""

import logging
from typing import Any, Dict, Optional, Union

# from app.core.security import get_password_hash, verify_password
from app.crud.crud_base import CRUDBase
from app.models.models_user import User
from app.schemas.schemas_user import UserCreate, UserUpdate

# get root logger
logger = logging.getLogger(__name__)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """
    CRUD CLASS - USER
    """

    def get_by_email(self, email: str) -> Optional[User]:
        """
        Method to retrieve user by email
        """
        return self.engine.find_one(self.model, self.model.email == email)
    

    def get_by_username(self, username: str) -> Optional[User]:
        """
        Method to retrieve user by username
        """
        return self.engine.find_one(self.model, self.model.username == username)



crud_user = CRUDUser(User)
