import time
from typing import Any
from uuid import UUID

from app.crud.base import CRUDBase
from app.models.asset import Asset
from app.schemas.asset import AssetCreate
from app.schemas.asset import AssetUpdate
from app.tasks.asset import process_asset
from sqlalchemy.orm import Session


class CRUDAsset(CRUDBase[Asset, AssetCreate, AssetUpdate]):
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
        asset: Asset = super().create(db, obj_in=obj_in)

        process_asset(asset)

        return asset


asset = CRUDAsset(Asset)
