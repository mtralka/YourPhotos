# from typing import TYPE_CHECKING

from email.policy import default
from enum import Enum
from enum import unique
from typing import Final

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import SmallInteger
from sqlalchemy import String
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship


# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401

# https://www.media.mit.edu/pia/Research/deepview/exif.html

# EXIF_TAGS: Final[dict[str, str]] = {
#     "image_description": "0x010e",
#     "make": "0x010f",
#     "model": "0x0110",
#     "x_resolution": "0x011a",
#     "y_resolution": "0x011b",
#     "resolution_unit": "0x0128",
#     "datetime": "0x0132",
# }

# class ExifTags(Enum):

# EXIF_LOOKUP: Final[dict[str,str]] = {
#     "make":"Make",
#     "model": "Model",
#     "x_resolution": "XResolution"
#     "y_resolution": "YResolution"


# }


class Exif(Base):
    id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(Integer)  # ForeignKey('asset.id')
    # asset = relationship("Asset", back_populates="exif")

    image_description = Column(String, nullable=True, default=None)
    make = Column(String, nullable=True, default=None)
    model = Column(String, nullable=True, default=None)
    x_resolution = Column(Float, nullable=True, default=None)
    y_resolution = Column(Float, nullable=True, default=None)
    resolution_unit = Column(SmallInteger, nullable=True, default=None)
    date_time = Column(String, nullable=True, default=None)
    copyright = Column(String, nullable=True, default=None)
    exposure_time = Column(Float, nullable=True, default=None)
    f_number = Column(Float, nullable=True, default=None)
    shutter_speed_value = Column(
        Float, nullable=True, default=None
    )  # To convert this value to ordinary 'Shutter Speed'; calculate this value's power of 2, then reciprocal
    aperture_value = Column(
        Float, nullable=True, default=None
    )  # To convert this value to ordinary F-number(F-stop), calculate this value's power of root 2
    flash = Column(SmallInteger, nullable=True, default=None)
    focal_length = Column(Float, nullable=True, default=None)  # in mm

    latitude = Column(Float, nullable=True, default=None)
    longitude = Column(Float, nullable=True, default=None)
    altitude = Column(Float, nullable=True, default=None)
