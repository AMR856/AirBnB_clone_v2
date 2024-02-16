#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv
from models.city import City
import models

class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey("places.id") ,nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

# for DBStorage: class attribute reviews must represent a relationship with the class Review. If 
# the Place object is deleted, all linked Review objects must be automatically deleted. Also, the 
# reference from a Review object to his Place should be named place
# for FileStorage: getter attribute reviews that returns the list of 
# Review instances with place_id equals to the current Place.id => It will be the FileStorage 
# relationship between Place and Review