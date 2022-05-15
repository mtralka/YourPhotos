import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship


class Geocode(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    asset_id = Column(UUID(as_uuid=True), ForeignKey("asset.id"), unique=True)
    asset = relationship("Asset", back_populates="geocode")

    address = Column(String, nullable=True, default=None)
    postcode = Column(String, nullable=True, default=None)
    place = Column(String, nullable=True, default=None)
    district = Column(String, nullable=True, default=None)
    region = Column(String, nullable=True, default=None)
    country = Column(String, nullable=True, default=None)
