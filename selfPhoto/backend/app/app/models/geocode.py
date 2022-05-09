from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship


class Geocode(Base):
    id = Column(Integer, primary_key=True, index=True)

    # asset_id = Column(Integer, ForeignKey("asset.id"))
    # asset = relationship("Asset", back_populates="geocode")
    # asset = relationship("Asset", backref=backref("geocode", uselist=False))
    # asset_id = Column(Integer, ForeignKey('asset.id'))
    # asset = relationship("Asset", back_populates="geocode", primaryjoin="Asset.id==Geocode.asset_id")
    asset_id = Column(Integer)

    address = Column(String, nullable=True, default=None)
    postcode = Column(String, nullable=True, default=None)
    place = Column(String, nullable=True, default=None)
    district = Column(String, nullable=True, default=None)
    region = Column(String, nullable=True, default=None)
    country = Column(String, nullable=True, default=None)
