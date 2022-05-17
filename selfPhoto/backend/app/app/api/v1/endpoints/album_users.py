from email.policy import default
from typing import Any
from uuid import UUID

from app import crud
from app import models
from app import schemas
from app.api import deps
from app.api.http_exceptions import raise_not_exists
from app.api.http_exceptions import raise_permissions_error
from app.auth_validators import AlbumUserAuthValidator
from app.regex import UUID_REGEX
from app.schemas.album_user import AlbumUser
from app.schemas.album_user import AlbumUserCreate
from app.schemas.album_user import AlbumUserUpdate
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
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
    Get a new album user share
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumUserAuthValidator.can_user_view(db, current_user, album):
        raise_permissions_error()

    # return all people who can view
    # CRUD

    return


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
    user_id: UUID = Query(
        default=...,
        title="User UUID",
        description="User UUID for the user you wish to share this album with",
    ),
) -> Any:
    """
    Create a new album user share
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumUserAuthValidator.can_user_create(db, current_user, album):
        raise_permissions_error()

    return crud.album.create(db, obj_in=AlbumUserCreate(album_id=id, owner_id=user_id))


@router.delete("/{id}/shares", status_code=204)
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
        description="User UUID for the user you wish to share this album with",
    ),
) -> Any:
    """
    Delete an existing album user share
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumUserAuthValidator.can_user_delete(db, current_user, album):
        raise_permissions_error()

    # CRUD
