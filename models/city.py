#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, storage_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_engine == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        name = ""
        state_id = ""
