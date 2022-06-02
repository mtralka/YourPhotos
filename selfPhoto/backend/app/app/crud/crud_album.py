from typing import Any
from uuid import UUID

from app import schemas
from app.crud.base import CRUDBase
from app.models import Album
from app.models import AlbumAsset
from app.models import AlbumUser
from app.models import Asset
from app.schemas import AlbumCreate
from app.schemas import AlbumUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func
from sqlalchemy.orm import Session


class CRUDAlbum(CRUDBase[Album, AlbumCreate, AlbumUpdate]):
    def get_multi_by_owner(self, db: Session, *, user_id: int) -> list[Album]:
        return (
            db.query(
                Album,
            )
            .filter(Album.owner_id == user_id)
            .all()
        )


album = CRUDAlbum(Album)
