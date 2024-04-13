#!/usr/bin/python3
"""
module that contains the class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class City(Base):
    """state class
    Attributes:
        __tablename__ (str): table name
        id (int): state id
        name (str): state name of class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
