from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class Asset(Base):
    id = Column(Integer, primary_key=True, index=True)
    content_type = Column(String, nullable=False)
    asset_path = Column(String, nullable=False)
    thumbnail_path = Column(String, nullable=True)

    file_size = Column(Integer)
    file_name = Column(String)
    file_extension = Column(String)

    created_at = Column(DateTime, nullable=False, default=func.now())
    modified_at = Column(DateTime, nullable=False, default=func.now())

    ##
    # User
    ##
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="assets")

    ##
    # Geocode
    ##
    # geocode = relationship("Geocode", back_populates="asset")
    # geocode = relationship("Geocode", back_populates="asset", uselist=False, primaryjoin="Asset.id==Geocode.asset_id")
