import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Request, Security, status

from app.authentication.password_hashing import Hash
from app.crud.crud_user import crud_user
from app.schemas.schemas_response import BaseResponse
from app.schemas.schemas_user import UserCreate, UserView

router = APIRouter(prefix="/users", tags=["Users"])
logger = logging.getLogger(__name__)

"""
    to get the list of all the users
"""

user_found = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="User already Exist!",
)


@router.get("/", response_model=BaseResponse)
async def get_all_users():
    data = await crud_user.get_multi_without_limit()
    print(data)
    return BaseResponse(success=True, message="List of all users", data=data)


@router.post("/")
async def register_user(
    request: Request,
    user_in: UserCreate,
    *,
    response_model=UserView,
):
    """
    API for Registering Users on the Platform
    """

    user = await crud_user.get_by_email(email=user_in.email)
    if user:
        logger.error("User with email %s has already registered!", user_in.email)
        raise user_found

    user_in.id = ObjectId()
    print(user_in.password, type(user_in.password))
    user_in.password = Hash.bcrypt(user_in.password)
    user = await crud_user.create(obj_in=user_in)

    return user
