from app.api import api_user
from app.authentication import oauth2
from app.core import database
from app.schemas import enums, schemas_user
from fastapi import APIRouter, BackgroundTasks, Depends, Security, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

"""
    to get the list of all the users
"""