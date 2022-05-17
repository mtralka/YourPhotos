from uuid import UUID

from app.crud.base import CRUDBase
from app.models import AlbumAsset
from app.models import Asset
from app.schemas import AlbumAssetCreate
from app.schemas import AlbumAssetUpdate
from sqlalchemy.orm import Session


class CRUDAlbumAsset(CRUDBase[AlbumAsset, AlbumAssetCreate, AlbumAssetUpdate]):
    def get_multi_by_album_id(
        self,
        db: Session,
        *,
        album_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Asset]:

        return (
            db.query(Asset)
            .select_from(AlbumAsset, Asset)
            .join(AlbumAsset)
            .filter(AlbumAsset.album_id == album_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def remove(self, db: Session, *, album_id: UUID, asset_id: UUID) -> Asset | None:
        obj = (
            db.query(AlbumAsset)
            .filter(AlbumAsset.album_id == album_id)
            .filter(AlbumAsset.asset_id == asset_id)
            .first()
        )

        if obj is None:
            return None

        db.delete(obj)
        db.commit()

        return obj


album_asset = CRUDAlbumAsset(AlbumAsset)
