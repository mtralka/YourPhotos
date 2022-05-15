from datetime import datetime
from uuid import UUID

from .base import CamelModel


class AlbumUserBase(CamelModel):
    asset_id: int
    address: str | None = None
    postcode: str | None = None
    place: str | None = None
    district: str | None = None
    region: str | None = None
    country: str | None = None


# Properties to receive on creation
class AlbumUserCreate(AlbumUserBase):
    album_id: UUID
    owner_id: UUID
    pass


# Properties to receive on update
class AlbumUserUpdate(AlbumUserBase):
    pass


class AlbumUserInDBBase(AlbumUserBase):
    id: UUID | None = None
    created_at: datetime | None = None
    modified_at: datetime | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class AlbumUser(AlbumUserInDBBase):
    pass
