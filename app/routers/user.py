import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Request, Security, status

from app.authentication.password_hashing import Hash
from app.crud.crud_user import crud_user
from app.schemas.schemas_response import BaseResponse
from app.schemas.schemas_user import UserCreate, UserView, UserUpdate

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
    return BaseResponse(success=True, message="List of all users", data=data)


@router.post("/", response_model=UserView)
async def register_user(user_in: UserCreate):
    """
    API for Registering Users on the Platform
    """
    if await crud_user.get_by_email(email=user_in.email):
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user_in.id = ObjectId()
    user_in.password = Hash.bcrypt(user_in.password)

    created_user = await crud_user.create(obj_in=user_in)

    return created_user


@router.patch("/{email}", response_model=UserView)
async def update_user(email: str, user_update: UserUpdate):
    """
    API for Updating User Information
    """
    user = await crud_user.get_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await crud_user.update(db_obj=user, obj_in=user_update)

    return updated_user




@router.get("/{email}", response_model=UserView)
async def get_user(email: str):
    """
    API for Retrieving User Information
    """
    # Retrieve the user by ID
    user = await crud_user.get_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user