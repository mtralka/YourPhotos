from app.db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class AlbumUser(Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="shared_albums")

    album_id = Column(UUID(as_uuid=True), ForeignKey("album.id"), index=True)

    can_edit_album = Column(Boolean, default=False, nullable=False)
    can_share_album = Column(Boolean, default=False, nullable=False)
    can_remove_assets = Column(Boolean, default=False, nullable=False)
    can_add_assets = Column(Boolean, default=False, nullable=False)
