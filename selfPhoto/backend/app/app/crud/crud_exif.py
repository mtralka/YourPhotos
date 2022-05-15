from typing import Any
from uuid import UUID

from app import models
from app.crud.base import CRUDBase
from app.models.exif import Exif
from app.schemas.exif import ExifCreate
from app.schemas.exif import ExifUpdate
from fastapi.encoders import jsonable_encoder
import humps
from sqlalchemy.orm import Session


class CRUDExif(CRUDBase[Exif, ExifCreate, ExifUpdate]):
    # def get_by_id(self, db: Session, *, id: UUID) -> Exif | None:
    #     return db.query(Exif).filter(Exif.id == id).first()

    # def get_by_hash(self, db: Session, *, hash: int) -> Asset | None:
    #     return db.query(Asset).filter(Asset.hash == hash).first()

    # def create(self, db: Session, *, obj_in: ExifCreate) -> Exif:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = Exif(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)

    #     return db_obj

    def update(
        self, db: Session, *, db_obj: Exif, obj_in: ExifUpdate | dict[str, Any]
    ) -> Exif:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    # def is_active(self, user: Asset) -> bool:
    #     return user.is_active

    # def is_superuser(self, user: Asset) -> bool:
    #     return user.is_superuser


exif = CRUDExif(Exif)
