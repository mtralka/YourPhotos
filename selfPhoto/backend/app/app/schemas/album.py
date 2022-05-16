from datetime import datetime
from uuid import UUID

from .base import CamelModel


class AlbumBase(CamelModel):
    name: str | None


# Properties to receive on creation
class AlbumCreate(AlbumBase):
    owner_id: UUID


# Properties to receive on update
class AlbumUpdate(AlbumBase):
    pass


class AlbumInDBBase(AlbumBase):
    id: UUID | None = None
    created_at: datetime | None = None
    modified_at: datetime | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Album(AlbumInDBBase):
    pass
