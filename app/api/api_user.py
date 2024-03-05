from app.authentication.password_hashing import Hash
from app.schemas import models, schemas_user
from fastapi import BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


def get_user_query(id: int, db: Session):
    user_query = db.query(models.User).filter(models.User.id == id)
    if user_query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with the ID {id} is not found!",
        )
    return user_query, user_query.first()
