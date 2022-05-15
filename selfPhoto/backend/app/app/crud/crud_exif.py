from typing import Any
from uuid import UUID

from app import models
from app.crud.base import CRUDBase
from app.models.exif import Exif
from app.schemas.exif import ExifCreate
from app.schemas.exif import ExifUpdate
from fastapi.encoders import jsonable_encoder
import humps
from sqlalchemy.orm import Session


class CRUDExif(CRUDBase[Exif, ExifCreate, ExifUpdate]):
    ...


exif = CRUDExif(Exif)
