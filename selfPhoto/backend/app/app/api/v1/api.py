# from app.api.v1.endpoints import items
from enum import Enum

from app.api.v1.endpoints import album
from app.api.v1.endpoints import album_users
from app.api.v1.endpoints import asset
from app.api.v1.endpoints import exif
from app.api.v1.endpoints import login
from app.api.v1.endpoints import media
from app.api.v1.endpoints import thumbnail
from app.api.v1.endpoints import users

# from app.api.v1.endpoints import utils
from fastapi import APIRouter


class Tags(Enum):
    assets = "assets"
    auth = "auth"
    album = "album"
    album_sharing = "album sharing"
    users = "users"


api_router = APIRouter()
api_router.include_router(login.router, tags=[Tags.auth])
api_router.include_router(users.router, prefix="/users", tags=[Tags.users])
api_router.include_router(asset.router, tags=[Tags.assets])
api_router.include_router(media.router, tags=[Tags.assets])
api_router.include_router(thumbnail.router, tags=[Tags.assets])
api_router.include_router(exif.router, tags=[Tags.assets])
api_router.include_router(album.router, tags=[Tags.album], prefix="/albums")
api_router.include_router(
    album_users.router, tags=[Tags.album_sharing], prefix="/albums"
)
