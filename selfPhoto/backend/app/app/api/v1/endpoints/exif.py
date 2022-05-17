from typing import Any

from app import crud
from app import models
from app import schemas
from app.api import deps
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

router = APIRouter()


@router.get("/assets/{id}/exif", response_model=schemas.Exif)
async def get_exif(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: str,
) -> Any:
    """
    Return an asset's exif data
    """

    if not (exif := crud.exif.get(db, id=UUID(id))):
        raise HTTPException(
            status_code=404,
            detail="Exif does not exist",
        )

    # TODO review this
    if not current_user.is_superuser and current_user.id != exif.asset_id:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges to access exif",
        )

    return exif
