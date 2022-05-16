import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Album(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    owner = relationship("User", back_populates="albums")

    created_at = Column(DateTime, nullable=False, default=func.now())
    modifed_at = Column(DateTime, nullable=False, default=func.now())

    name = Column(String, nullable=True, default=None)

    album_users = relationship("AlbumUser", cascade="all, delete")
    album_assets = relationship("AlbumAsset", cascade="all, delete")
