from typing import Any
from uuid import UUID

from app import crud
from app import models
from app.api import deps
from app.api.http_exceptions import raise_not_exists
from app.api.http_exceptions import raise_permissions_error
from app.auth_validators import AlbumUserAuthValidator
from app.schemas.album_user import AlbumUser
from app.schemas.album_user import AlbumUserCreate
from app.schemas.album_user import AlbumUserUpdate
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path
from fastapi import Query
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/{id}/shares", response_model=list[AlbumUser])
async def get_all_album_shared_users(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
) -> Any:
    """
    Get all shares for album
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumUserAuthValidator.can_user_view(db, current_user, album):
        raise_permissions_error()

    return [user for user in crud.album_user.get_by_album_id(db, album_id=album.id)]


@router.post("/{id}/shares", response_model=AlbumUser)
async def create_album_user_share(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    user_id: UUID = Body(..., alias="userId"),
    can_edit_album: bool = Body(default=False, alias="canEditAlbum"),
    can_share_album: bool = Body(default=False, alias="canShareAlbum"),
    can_remove_assets: bool = Body(default=False, alias="canRemoveAssets"),
    can_add_assets: bool = Body(default=False, alias="canAddAssets"),
) -> Any:
    """
    Create a new album user share
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumUserAuthValidator.can_user_create(db, current_user, album):
        raise_permissions_error()

    return crud.album_user.create(
        db,
        obj_in=AlbumUserCreate(
            album_id=id,
            user_id=user_id,
            can_edit_album=can_edit_album,
            can_share_album=can_share_album,
            can_remove_assets=can_remove_assets,
            can_add_assets=can_add_assets,
        ),
    )


@router.delete("/{id}/shares", responses={204: {"model": None}})
async def delete_album_user_share(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    user_id: UUID = Query(
        default=...,
        title="User UUID",
        alias="userId",
        description="User UUID for the user you wish to share this album with",
    ),
) -> Any:
    """
    Delete an existing album user share
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if (
        album_user := crud.album_user.get_by_id(db, user_id=user_id, album_id=id)
    ) is None:
        raise_not_exists("album user")

    if not AlbumUserAuthValidator.can_user_delete(db, current_user, album, album_user):
        raise_permissions_error()

    crud.album_user.remove(db, obj=album_user)

    pass


@router.put("/{id}/shares/{user_id}", response_model=AlbumUser)
async def update_album_user(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    user_id: UUID = Path(
        default=...,
        title="User UUID",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
        description="User UUID for the user you wish to edit share settings",
    ),
    album_user_in: AlbumUserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an album user.
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if (
        album_user := crud.album_user.get_by_id(db, user_id=user_id, album_id=id)
    ) is None:
        raise_not_exists("album user")

    if not AlbumUserAuthValidator.can_user_edit(db, current_user, album):
        raise_permissions_error()

    return crud.album_user.update(db, db_obj=album_user, obj_in=album_user_in)
