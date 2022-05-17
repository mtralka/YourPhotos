from datetime import datetime
from uuid import UUID

from .base import CamelModel


class AlbumUserBase(CamelModel):
    is_editor: bool


# Properties to receive on creation
class AlbumUserCreate(AlbumUserBase):
    album_id: UUID
    owner_id: UUID


# Properties to receive on update
class AlbumUserUpdate(AlbumUserBase):
    pass


class AlbumUserInDBBase(AlbumUserBase):
    id: UUID | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class AlbumUser(AlbumUserInDBBase):
    pass
