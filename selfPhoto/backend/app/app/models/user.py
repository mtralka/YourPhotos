# from typing import TYPE_CHECKING
import uuid

from app.db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class User(Base):
    # id = Column(Integer, primary_key=True, index=True)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    # items = relationship("Item", back_populates="owner")

    # assets = relationship("Asset")
    assets = relationship("Asset", back_populates="user")

    albums = relationship("Album", back_populates="owner", uselist=False)
    shared_albums = relationship("AlbumUser", back_populates="user")
