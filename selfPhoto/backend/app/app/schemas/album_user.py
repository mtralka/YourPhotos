from uuid import UUID

from .base import CamelModel


class AlbumUserBase(CamelModel):
    album_id: UUID
    user_id: UUID
    can_edit_album: bool
    can_share_album: bool
    can_remove_assets: bool
    can_add_assets: bool


# Properties to receive on creation
class AlbumUserCreate(AlbumUserBase):
    pass


# Properties to receive on update
class AlbumUserUpdate(CamelModel):
    can_edit_album: bool | None
    can_share_album: bool | None
    can_remove_assets: bool | None
    can_add_assets: bool | None


class AlbumUserInDBBase(AlbumUserBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class AlbumUser(AlbumUserInDBBase):
    pass
