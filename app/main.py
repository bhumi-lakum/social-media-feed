from app.core.config import settings
from app.core.database import engine
from app.routers import authentication, user
from app.schemas import models
from fastapi import APIRouter, FastAPI

app = FastAPI(
    title=settings.APPLICATION_TITLE,
    version=settings.APPLICATION_VERSION,
    contact={
        "name": "",
        "email": "",
    },
    openapi_url=f"{settings.APPLICATION_API_VERSION}/openapi.json",
    docs_url="/documentation",
    redoc_url=None,
)

models.Base.metadata.create_all(engine)

router = APIRouter()

# include all routers
router.include_router(authentication.router)
router.include_router(user.router)

app.include_router(router, prefix=settings.APPLICATION_API_VERSION)
