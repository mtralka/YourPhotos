from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Album(Base):
    id = Column(String, primary_key=True, index=True)

    asset_id = Column(String)
    owner_id = Column(String, index=True)

    created_at = Column(DateTime, nullable=False, default=func.now())
    modifed_at = Column(DateTime, nullable=False, default=func.now())

    name = Column(String, nullable=True, default=None)
