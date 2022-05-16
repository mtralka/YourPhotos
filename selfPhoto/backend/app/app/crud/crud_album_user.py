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
        return (
            db.query(AlbumUser)
            .filter(AlbumUser.album_id == album_id)
        )


album_user = CRUDAlbumUser(AlbumUser)

    # def get_eligble_viewers(self, db: Session, *, album_id: UUID) -> list[AlbumUser]:
    #     return (
    #         db.query(AlbumUser)
    #         .filter(AlbumUser.album_id == album_id)
    #     )

    # def get_eligble_editors(self, db: Session, *, album_id: UUID) -> list[AlbumUser]:
    #     return (
    #         db.query(AlbumUser)
    #         .filter(AlbumUser.album_id == album_id)
    #         .filter(AlbumUser.is_editor == True)
    #     )
