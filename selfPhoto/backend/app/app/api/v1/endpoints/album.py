from typing import Any
from uuid import UUID

from app import crud
from app import models
from app import schemas
from app.api import deps
from app.api.http_exceptions import raise_not_exists
from app.api.http_exceptions import raise_permissions_error
from app.auth_validators import AlbumAuthValidator
from app.schemas.album import AlbumCreate
from app.schemas.album_asset import AlbumAssetCreate
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path
from fastapi import Query
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/", response_model=schemas.Album)
async def create_album(
    *,
    db: Session = Depends(deps.get_db),
    album_in: AlbumCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create a new album
    """

    if not AlbumAuthValidator.can_user_create(db, current_user):
        raise_permissions_error()

    return crud.album.create(db, obj_in=AlbumCreate(**album_in))


@router.delete("/{id}", responses={204: {"model": None}})
async def delete_album(
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
    Delete an album
    """
    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumAuthValidator.can_user_delete(db, current_user, album):
        raise_permissions_error()

    crud.album.remove(db, obj=album)

    pass


@router.put("/{id}", response_model=schemas.Album)
def update_album(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    album_in: schemas.AlbumUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an album.
    """
    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumAuthValidator.can_user_edit(db, current_user, album):
        raise_permissions_error()

    album = crud.album.update(db, db_obj=album, obj_in=album_in)
    return album


@router.post("/{id}/assets", response_model=schemas.AlbumAsset)
async def add_asset_to_album(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    asset_id: UUID = Body(..., alias="assetId"),
) -> Any:
    """
    Add assets by UUID to album
    """
    # TODO make this work with lists

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumAuthValidator.can_user_add_assets(db, user=current_user, album=album):
        raise_permissions_error()

    return crud.album_asset.create(
        db, obj_in=AlbumAssetCreate(album_id=id, asset_id=asset_id)
    )


@router.delete("/{id}/assets", responses={204: {"model": None}})
async def remove_asset(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    assets: UUID = Query(
        default=...,
        title="User UUIDs",
        description="List of asset UUIDs you wish to remove from this album",
    ),
) -> Any:
    """
    Add asset by UUID to album
    """
    # TODO make this work with query lists
    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumAuthValidator.can_user_remove_assets(
        db, user=current_user, album=album
    ):
        raise_permissions_error()

    if not isinstance(assets, list):
        assets = [assets]

    for asset in assets:
        crud.album_asset.remove(db, album_id=id, asset_id=asset)

    pass


@router.get("/", response_model=list[schemas.Album])
async def get_all_albums(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get all albums
    """

    return crud.album.get_multi_by_owner(db, user_id=current_user.id)


@router.get("/{id}", response_model=schemas.Album)
async def get_album_info(
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
    Retrieve album info
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumAuthValidator.can_user_view(db, current_user, album):
        raise_permissions_error()

    return album


@router.get("/{id}/assets")
async def get_album_assets(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID = Path(
        default=...,
        title="UUID of target album",
        example="e8e99722-740e-4355-b18b-82da5b995cc1",
    ),
    skip: int = Query(
        default=0, title="Skip", description="Number of assets to skip", example=120
    ),
    limit: int = Query(
        default=100,
        title="Response Limit",
        description="Maximum amount of assets to return",
        example=25,
    ),
) -> Any:
    """
    Retrieve album assets
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise_not_exists("album")

    if not AlbumAuthValidator.can_user_view(db, current_user, album):
        raise_permissions_error()

    return crud.album_asset.get_multi_by_album_id(
        db, album_id=id, skip=skip, limit=limit
    )
