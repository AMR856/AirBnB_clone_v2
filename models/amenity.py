#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv
from models.city import City
import models


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
