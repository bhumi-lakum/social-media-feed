from app.core.config import settings
from app.routers import authentication, user
from fastapi import APIRouter, FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


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


router = APIRouter()

# include all routers
router.include_router(authentication.router)
router.include_router(user.router)

app.include_router(router, prefix=settings.APPLICATION_API_VERSION)
