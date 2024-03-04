from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.authentication import auth_token
from app.authentication.password_hashing import Hash
from app.core import database
from app.models.models_user import User

router = APIRouter(tags=["Authentication"])


"""
    user login
"""


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    access_token = auth_token.create_access_token(
        data={"sub": user.email, "user_type": user.user_type.value}
    )
    return {"access_token": access_token, "token_type": "bearer"}
