from xmlrpc.client import Boolean

from app.db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class AlbumUser(Base):
    id = Column(String, primary_key=True, index=True)

    album_id = Column(String, index=True)
    owner_id = Column(String, index=True)

    editor = Column(Boolean, default=False, nullable=False)
