#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, String, Integer


Base = declarative_base()


class City(Base):
    """
        City class inherits the Base class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
