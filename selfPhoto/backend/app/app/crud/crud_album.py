from typing import Any
from uuid import UUID

from app.crud.base import CRUDBase
from app.models import Album
from app.schemas import AlbumCreate
from app.schemas import AlbumUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDAlbum(CRUDBase[Album, AlbumCreate, AlbumUpdate]):
    ...


album = CRUDAlbum(Album)
