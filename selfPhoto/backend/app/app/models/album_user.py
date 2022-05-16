import uuid

from app.db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class AlbumUser(Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="shared_albums")

    album_id = Column(UUID(as_uuid=True), ForeignKey("album.id"), index=True)
    #  album = relationship("Album", back_populates="shared_albums")

    is_editor = Column(Boolean, default=False, nullable=False)

    # can_remove_assets
    # can_add_assets