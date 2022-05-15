from pathlib import Path
from typing import Any
from uuid import UUID

import aiofiles
from app import crud
from app import models
from app import schemas
from app.api import deps
from app.core.config import settings
from app.schemas import AssetCreate
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session


# curl -X 'POST' 'http://localhost:8000/api/v1/assets/' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTMyNjMyNjMsInN1YiI6ImNmNGI3NjNhLTU3YmUtNDI5Ni1iZGVmLTNjZTcxOWU3NjZlNCJ9.XDmoo3OsJ0MkiXZig1rygDT2H8e8OU9OSnSn31TAaEk' -H 'Content-Type: multipart/form-data' -F 'assets=@C:\Users\mtral\Downloads\placeholder_photos\pexels-alexander-ant-5603660.jpg;type=image/jpeg'

router = APIRouter()


@router.post("/asset", response_model=schemas.Asset)
async def create_asset(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    asset: UploadFile,
) -> Any:
    """
    Create a new asset
    """

    return await handle_file_upload(db, current_user, asset)


@router.post("/assets/", response_model=list[schemas.Asset])
async def create_assets(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    assets: list[UploadFile],
) -> Any:
    """
    Create new assets
    """

    generated_assets: list[models.Asset] = []
    for asset in assets:
        new_asset: models.Asset = await handle_file_upload(db, current_user, asset)
        generated_assets.append(new_asset)

    return generated_assets


@router.get("/asset/{id}", response_model=schemas.Asset)
async def get_asset_by_id(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: str,
) -> Any:
    """
    Return an asset by ID
    """

    asset: schemas.Asset | None = crud.asset.get_by_id(db, id=UUID(id))

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset does not exist",
        )

    if not current_user.is_superuser or current_user.id != asset.user_id:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges to access asset",
        )

    return asset


@router.get("/assets", response_model=list[schemas.Asset])
async def get_assets(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Return multiple assets controled by skip and limit
    """

    # TODO
    # add album id modifier
    # add onlyFavoritesTag
    if current_user.is_superuser:
        assets = crud.asset.get_multi(db, skip=skip, limit=limit)
    else:
        assets = crud.asset.get_multi_by_owner(
            db, user_id=current_user.id, skip=skip, limit=limit
        )

    return assets


async def handle_file_upload(
    db: Session, current_user: models.user, asset: UploadFile
) -> models.Asset:

    asset_filepath: Path = (
        settings.DATA_DIR / str(current_user.id) / "assets" / asset.filename
    )

    if asset_filepath.exists():
        # TODO handle
        print("exists")

    file_size: int
    async with aiofiles.open(asset_filepath, "wb") as out:
        contents = await asset.read()
        await out.write(contents)

        file_size = len(contents)

    return crud.asset.create(
        db,
        obj_in=AssetCreate(
            asset_path=str(asset_filepath),
            content_type=asset.content_type,
            file_size=file_size,
            user_id=current_user.id,
            file_name=asset_filepath.stem,
            file_extension=asset_filepath.suffix,
        ),
    )
