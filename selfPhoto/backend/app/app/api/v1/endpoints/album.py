# add asset to album
# remove asset from album
# create album

from typing import Any
from uuid import UUID

from app import crud
from app import models
from app import schemas
from app.api import deps
from app.auth_validators import AlbumAuthValidator
from app.schemas import AssetCreate
from app.schemas.album import AlbumCreate
from app.schemas.album_asset import AlbumAssetCreate
from app.schemas.album_user import AlbumUserCreate
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/create", response_model=schemas.Album)
async def create_album(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    name: str | None
) -> Any:
    """
    Create a new album
    """

    return crud.album.create(
        db, obj_in=AlbumCreate(name=name, owner_id=current_user.id)
    )

@router.post("/{id}/add", response_model=list[schemas.AlbumAsset] )
async def add_asset_to_album(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID,
    asset: UUID
) -> Any:
    """
    Add asset by UUID to album 
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise HTTPException(
            status_code=404,
            detail="Album does not exist",
        )

    if not AlbumAuthValidator.can_user_add_assets(db, user=current_user, album=album):
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges",
        )

    return crud.album_asset.create(db, obj_in=AlbumAssetCreate(
    album_id = id,
    asset_id = asset
    ))


@router.get("/" , response_model=list[schemas.Album])
async def get_all_albums(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get all albums
    """
  
    return crud.album.get_multi_by_owner(db, user_id=current_user.id)


@router.get("/{id}/", response_model=schemas.Album)
async def get_album_info(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID
) -> Any:
    """
    Retrieve album info
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise HTTPException(
            status_code=404,
            detail="Album does not exist",
        )

    if not AlbumAuthValidator.can_user_view(db, user=current_user, album=album):
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges",
        )

    return album


@router.get("/{id}/assets")
async def get_album_assets(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: UUID,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve album
    """

    if (album := crud.album.get_by_id(db, id=id)) is None:
        raise HTTPException(
            status_code=404,
            detail="Album does not exist",
        )

    if not AlbumAuthValidator.can_user_view(db, user=current_user, album=album):
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges",
        )

    return crud.album_asset.get_multi_by_album_id(db, album_id=id, skip=skip, limit=limit)
