from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class AlbumAsset(Base):
    album_id = Column(UUID(as_uuid=True), ForeignKey("album.id"), primary_key=True)
    album = relationship("Album", back_populates="album_assets")

    asset_id = Column(UUID(as_uuid=True), ForeignKey("asset.id"), primary_key=True)
    asset = relationship("Asset", back_populates="albums")
    # asset = relationship("Asset", backref=backref("asset"))

    created_at = Column(DateTime, nullable=False, default=func.now())
