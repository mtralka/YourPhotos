import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Asset(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    content_type = Column(String, nullable=False)
    asset_path = Column(String, nullable=False)
    thumbnail_path = Column(String, nullable=True)

    file_size = Column(Integer)
    file_name = Column(String)
    file_extension = Column(String)

    created_at = Column(DateTime, nullable=False, default=func.now())
    modified_at = Column(DateTime, nullable=False, default=func.now())

    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="assets")

    exif = relationship(
        "Exif", back_populates="asset", uselist=False, cascade="all, delete"
    )
    geocode = relationship(
        "Geocode", back_populates="asset", uselist=False, cascade="all, delete"
    )

    albums = relationship("AlbumAsset", cascade="all, delete", back_populates="asset")

    ##
    # Geocode
    ##
    # geocode = relationship("Geocode", back_populates="asset")
    # geocode = relationship("Geocode", back_populates="asset", uselist=False, primaryjoin="Asset.id==Geocode.asset_id")
