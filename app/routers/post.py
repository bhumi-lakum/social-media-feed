import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from app.crud.crud_post import crud_post
from app.schemas.schemas_response import BaseResponse
from app.schemas.schemas_post import PostCreate, PostView

router = APIRouter(prefix="/posts", tags=["Posts"])
logger = logging.getLogger(__name__)

"""
    to get the list of all the users
"""

user_found = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="User already Exist!",
)


@router.get("/", response_model=BaseResponse)
async def get_all_posts():
    data = await crud_post.get_multi_without_limit()
    return BaseResponse(success=True, message="List of all posts", data=data)




@router.post("/", response_model=PostView)
async def create_post(post_in: PostCreate):
    """
    API for Creating Posts on the Platform
    """
    created_post = await crud_post.create(obj_in=post_in)

    return created_post


# @router.get("/{post_id}", response_model=PostView)
# async def create_post(post_id: str):
#     """
#     API for Creating Posts on the Platform
#     """
#     created_post = await crud_post.get(obj_in=post_id)

#     return created_post