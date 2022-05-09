from datetime import datetime

from .base import CamelModel

class AssetBase(CamelModel):
    asset_path: str
    content_type: str
    file_size: int
    user_id: int
    file_name: str
    file_extension: str
    thumbnail_path: str | None


# Properties to receive on creation
class AssetCreate(AssetBase):
    pass


# Properties to receive on update
class AssetUpdate(CamelModel):
    thumbnail_path: str | None
    modified_at: datetime | None = None


class AssetInDBBase(AssetBase):
    id: int | None = None
    created_at: datetime | None = None
    modified_at: datetime | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Asset(AssetInDBBase):
    pass
