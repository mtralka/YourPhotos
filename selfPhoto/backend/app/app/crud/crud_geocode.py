from typing import Any
from uuid import UUID

from app.crud.base import CRUDBase
from app.models import Geocode
from app.schemas import GeocodeCreate
from app.schemas import GeocodeUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDGeocode(CRUDBase[Geocode, GeocodeCreate, GeocodeUpdate]):
   ...


geocode = CRUDGeocode(Geocode)
