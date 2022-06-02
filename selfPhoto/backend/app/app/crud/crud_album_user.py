from typing import Any
from uuid import UUID

from app.crud.base import CRUDBase
from app.models import AlbumUser
from app.schemas import AlbumUserCreate
from app.schemas import AlbumUserUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDAlbumUser(CRUDBase[AlbumUser, AlbumUserCreate, AlbumUserUpdate]):
    def get_by_album_id(self, db: Session, *, album_id: UUID) -> list[AlbumUser]:
        return db.query(AlbumUser).filter(AlbumUser.album_id == album_id)

    def get_by_id(
        self, db: Session, *, user_id: UUID | str, album_id: UUID | str
    ) -> AlbumUser | None:

        if isinstance(user_id, str):
            user_id = UUID(user_id)

        if isinstance(album_id, str):
            album_id = UUID(album_id)

        return (
            db.query(AlbumUser)
            .filter(AlbumUser.album_id == album_id, AlbumUser.user_id == user_id)
            .first()
        )


album_user = CRUDAlbumUser(AlbumUser)
