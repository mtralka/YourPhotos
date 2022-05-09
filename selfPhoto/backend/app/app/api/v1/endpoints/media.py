from pathlib import Path
from typing import Any

from app import crud
from app import models
from app.api import deps
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/{id}", response_class=FileResponse)
async def get_media(
    *,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_user),
    id: int
) -> Any:
    """
    Return an asset's media
    """

    asset: models.Asset | None = crud.asset.get_by_id(db, id=id)

    if not asset or not Path(asset.asset_path).exists():
        raise HTTPException(
            status_code=404,
            detail="Asset does not exist",
        )

    # if not current_user.is_superuser or current_user.id != asset.user_id:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="The user doesn't have enough privileges to access asset",
    #     )

    return asset.asset_path
