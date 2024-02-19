#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv
from models.city import City
import models

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref='user', cascade='delete')
    reviews = relationship("Review", backref='user', cascade='delete')