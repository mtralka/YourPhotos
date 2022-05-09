from typing import Any

from app.crud.base import CRUDBase
from app.models import Geocode
from app.schemas import GeocodeCreate
from app.schemas import GeocodeUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CRUDGeocode(CRUDBase[Geocode, GeocodeCreate, GeocodeUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Geocode | None:
        return db.query(Geocode).filter(Geocode.id == id).first()

    # def create(self, db: Session, *, obj_in: GeocodeCreate) -> Geocode:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = Geocode(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)

    #     return db_obj

    def update(
        self, db: Session, *, db_obj: Geocode, obj_in: GeocodeCreate | dict[str, Any]
    ) -> Geocode:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


geocode = CRUDGeocode(Geocode)
