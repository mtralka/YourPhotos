from datetime import datetime
from uuid import UUID

from .base import CamelModel


class AlbumAssetBase(CamelModel):
    pass


# Properties to receive on creation
class AlbumAssetCreate(AlbumAssetBase):
    album_id: UUID
    asset_id: UUID


# Properties to receive on update
class AlbumAssetUpdate(AlbumAssetBase):
    pass


class AlbumAssetInDBBase(AlbumAssetCreate):
    created_at: datetime | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class AlbumAsset(AlbumAssetInDBBase):
    pass
