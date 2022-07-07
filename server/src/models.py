from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    short_id = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    secret = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
