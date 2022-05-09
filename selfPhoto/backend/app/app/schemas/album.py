from .base import CamelModel

class Album(CamelModel):
    asset_id: int
    address: str | None = None
    postcode: str | None = None
    place: str | None = None
    district: str | None = None
    region: str | None = None
    country: str | None = None


# Properties to receive on creation
class GeocodeCreate(GeocodeBase):
    pass


# Properties to receive on update
class GeocodeUpdate(GeocodeBase):
    pass


class GeocodeInDBBase(GeocodeBase):
    id: int | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Geocode(GeocodeInDBBase):
    pass
