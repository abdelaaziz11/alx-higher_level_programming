#!/usr/bin/python3

from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer
from model_state import Base


class City(Base):
    """
        City class inherits the Base class
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
