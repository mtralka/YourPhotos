from uuid import UUID

from .base import CamelModel


class GeocodeBase(CamelModel):
    address: str | None = None
    postcode: str | None = None
    place: str | None = None
    district: str | None = None
    region: str | None = None
    country: str | None = None


# Properties to receive on creation
class GeocodeCreate(GeocodeBase):
    asset_id: UUID


# Properties to receive on update
class GeocodeUpdate(GeocodeBase):
    pass


class GeocodeInDBBase(GeocodeBase):
    id: UUID | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Geocode(GeocodeInDBBase):
    pass
