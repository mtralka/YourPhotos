# from typing import TYPE_CHECKING

from email.policy import default
from enum import Enum
from enum import unique
from typing import Final
import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import SmallInteger
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship


# https://www.media.mit.edu/pia/Research/deepview/exif.html


class Exif(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    asset_id = Column(UUID(as_uuid=True), ForeignKey("asset.id"), unique=True)
    asset = relationship("Asset", back_populates="exif")
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
