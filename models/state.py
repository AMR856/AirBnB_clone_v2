#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            theReturnedList = []
            pass

# for DBStorage: class attribute cities must represent a relationship with the class City. 
# If the State object is deleted, all linked City objects must 
# be automatically deleted. Also, the reference from a City object to his State should be named state
# for FileStorage: getter attribute cities that returns the list of City 
# instances with state_id equals to the current State.id => It will be the 
# FileStorage relationship between State and City

    # if getenv("HBNB_TYPE_STORAGE") != "db":
    #     @property
    #     def cities(self):
    #         """Get a list of all related City objects."""
    #         city_list = []
    #         for city in list(models.storage.all(City).values()):
    #             if city.state_id == self.id:
    #                 city_list.append(city)
    #         return city_list