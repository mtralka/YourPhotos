# add asset to album
# remove asset from album
# create album
# get paginated album
# download assets from album
from typing import Any

from app import crud
from app import models
from app import schemas
from app.api import deps
from app.schemas import AssetCreate
from app.schemas.album import AlbumCreate
from app.schemas.album_user import AlbumUserCreate
from fastapi import APIRouter
from fastapi import Depends
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
