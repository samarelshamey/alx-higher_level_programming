#!/usr/bin/python3
"""
module that contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """city class
    Attributes:
        __tablename__ (str): table name
        id (int): city id
        state_id: state id
        name (str): city name of class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
