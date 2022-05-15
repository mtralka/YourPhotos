from typing import Any

from app.crud.base import CRUDBase
from app.models import AlbumUser
from app.schemas import AlbumUserCreate
from app.schemas import AlbumUserUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDAlbumUser(CRUDBase[AlbumUser, AlbumUserCreate, AlbumUserUpdate]):
    ...

album_user = CRUDAlbumUser(AlbumUser)
