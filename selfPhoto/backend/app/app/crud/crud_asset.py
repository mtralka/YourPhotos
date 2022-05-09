import time
from typing import Any

from app.crud.base import CRUDBase
from app.models.asset import Asset
from app.schemas.asset import AssetCreate
from app.schemas.asset import AssetUpdate
from app.tasks.asset import process_asset
from sqlalchemy.orm import Session


class CRUDAsset(CRUDBase[Asset, AssetCreate, AssetUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Asset | None:
        return db.query(Asset).filter(Asset.id == id).first()

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Asset]:
        return (
            db.query(self.model)
            .filter(Asset.thumbnail_path != None)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> list[Asset]:
        return (
            db.query(Asset)
            .filter(Asset.user_id == owner_id)
            .filter(Asset.thumbnail_path != None)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, db: Session, *, obj_in: AssetCreate) -> Asset:
        db_obj = Asset(
            content_type=obj_in.content_type,
            asset_path=obj_in.asset_path,
            file_size=obj_in.file_size,
            user_id=obj_in.user_id,
            file_name=obj_in.file_name,
            file_extension=obj_in.file_extension,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        process_asset(db_obj.id)

        return db_obj

    def update(
        self, db: Session, *, db_obj: Asset, obj_in: AssetUpdate | dict[str, Any]
    ) -> Asset:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    # def is_active(self, user: Asset) -> bool:
    #     return user.is_active

    # def is_superuser(self, user: Asset) -> bool:
    #     return user.is_superuser


asset = CRUDAsset(Asset)
