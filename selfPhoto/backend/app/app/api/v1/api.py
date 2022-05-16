# from app.api.v1.endpoints import items
from app.api.v1.endpoints import album
from app.api.v1.endpoints import asset
from app.api.v1.endpoints import exif
from app.api.v1.endpoints import login
from app.api.v1.endpoints import media
from app.api.v1.endpoints import thumbnail
from app.api.v1.endpoints import users
# from app.api.v1.endpoints import utils
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])  # prefixed locally
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(asset.router, tags=["asset"])  # prefixed locally
api_router.include_router(media.router, tags=["media"], prefix="/media")
api_router.include_router(thumbnail.router, tags=["thumbnail"], prefix="/thumbnail")
api_router.include_router(exif.router, tags=["exif"], prefix="/exif")
api_router.include_router(album.router, tags=["album"], prefix="/albums")
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
