# coding: utf-8
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from app.persistence.database import Base


class Station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True)
    station_name = Column(String(64), nullable=False)
    address = Column(String(256))
    detail_address = Column(String(128))
    lat = Column(String(32))
    lng = Column(String(32))
