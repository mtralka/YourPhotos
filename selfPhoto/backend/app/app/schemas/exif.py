from uuid import UUID

from .base import CamelModel


class ExifBase(CamelModel):
    image_description: str | None = None
    make: str | None = None
    model: str | None = None
    x_resolution: float | None = None
    y_resolution: float | None = None
    resolution_unit: int | None = None
    date_time: str | None = None
    copyright: str | None = None
    exposure_time: float | None = None
    f_number: float | None = None
    shutter_speed_value: float | None = None
    aperture_value: float | None = None
    flash: int | None = None
    focal_length: float | None = None
    latitude: float | None = None
    longitude: float | None = None
    altitude: float | None = None


# Properties to receive on creation
class ExifCreate(ExifBase):
    asset_id: UUID


# Properties to receive on update
class ExifUpdate(ExifBase):
    pass


class ExifInDBBase(ExifBase):
    id: UUID | None = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Exif(ExifBase):
    class Config:
        orm_mode = True
