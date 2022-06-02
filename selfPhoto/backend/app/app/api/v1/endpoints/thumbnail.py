from pathlib import Path
from typing import Any
from uuid import UUID

from app import crud
from app import models
from app.api import deps
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/assets/{id}/thumbnail", response_class=FileResponse)
async def get_thumbnail(
    *,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_user),
    id: str
) -> Any:
    """
    Return an asset's thumbnail
    """

    asset: models.Asset | None = crud.asset.get_by_id(db, id=UUID(id))

    if not asset or not Path(asset.thumbnail_path).exists():
        raise HTTPException(
            status_code=404,
            detail="Asset does not exist",
        )

    # if not current_user.is_superuser or current_user.id != asset.user_id:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="The user doesn't have enough privileges to access asset",
    #     )

    if not asset.thumbnail_path:
        return

    return asset.thumbnail_path
