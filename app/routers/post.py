import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from app.core.ws_manager import connection_manager
from app.crud.crud_post import crud_post
from app.schemas.schemas_post import PostCreate, PostUpdate, PostView, PersonalizedPost
from app.schemas.schemas_response import BaseResponse

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
    """
    API for Retrieving all Posts on the Platform
    """
    data = await crud_post.get_multi_without_limit()
    return BaseResponse(success=True, message="List of all posts", data=data)


@router.post("/", response_model=PostView)
async def create_post(post_in: PostCreate):
    """
    API for Creating Posts on the Platform
    """
    created_post = await crud_post.create(obj_in=post_in)

    socket_message = {"type": "new_post", "data": created_post.dict()}

    await connection_manager.broadcast_message(f"{socket_message}")

    return created_post


@router.get("/{post_id}", response_model=PostView)
async def get_post(post_id: str):
    """
    API for Retrieving a Post on the Platform
    """
    post = await crud_post.get(ObjectId(post_id))

    return post


@router.patch("/{post_id}", response_model=PostView)
async def update_post(post_id: str, user_update: PostUpdate):
    """
    API for updating a Post on the Platform
    """
    post = await crud_post.get(ObjectId(post_id))
    updated_post = await crud_post.update(db_obj=post, obj_in=user_update)

    return updated_post


@router.delete("/{post_id}")
async def delete_post(post_id: str):
    """
    API for Deleting Post on the Platform
    """
    post = await crud_post.get(ObjectId(post_id))
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    await crud_post.remove(post)
    return {"message": "Post deleted successfully"}


@router.get("/personalized_feed/{author_id}", response_model=PersonalizedPost)
async def get_post(author_id: str, skip: int = 0, limit: int = 50):
    """
    API for Retrieving personalized feed for the login user
    """
    post = await crud_post.get_personised_posts(ObjectId(author_id), skip, limit)

    return {"posts": post, "skip": skip, "limit": limit}
