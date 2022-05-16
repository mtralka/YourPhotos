from typing import Any
from uuid import UUID

from app.crud.base import CRUDBase
from app.models import AlbumAsset
from app.models import Asset
from app.schemas import AlbumAssetCreate
from app.schemas import AlbumAssetUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDAlbumAsset(CRUDBase[AlbumAsset, AlbumAssetCreate, AlbumAssetUpdate]):
     def get_multi_by_album_id(self, db: Session, *, album_id: UUID, skip: int = 0, limit: int = 100, ) -> list[Asset]:

        return db.query(Asset).select_from(AlbumAsset, Asset).join(AlbumAsset).filter(AlbumAsset.album_id == album_id).offset(skip).limit(limit).all()

album_asset = CRUDAlbumAsset(AlbumAsset)
