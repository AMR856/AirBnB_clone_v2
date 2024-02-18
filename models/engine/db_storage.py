#!/usr/bin/python3
"""This module defines a class to manage the db storage for hbnb clone"""
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """A class here"""
    __engine = None
    __session = None

    def __init__(self):
        """The init function of the class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv("HBNB_MYSQL_USER"),
                                                                    getenv("HBNB_MYSQL_PWD"),
                                                                    getenv("HBNB_MYSQL_HOST"),
                                                                    getenv("HBNB_MYSQL_DB")),
                                                                    pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """A function to get objects"""
        objs = []
        myDic = {}
        if cls is None:
            for table in Base.metadata.tables.values():
                model_class = table.mapped_class
                records = self.__engine.query(model_class).all()
                objs.extend(records)
        else:
            if cls is str:
                classObject = eval(cls)
            obj = self.__session.query(classObject).all()
        for obj in objs:
            classType = type(obj)
            theKey = "{}.{}".format(classType.__name__, obj.id)
            myDic[theKey] = obj
        return myDic
    def new(self, obj):
        """A function to add an object"""
        self.__session.add(obj)
    def save(self):
        """A committer function"""
        self.__session.commit()
    def delete(self , obj=None):
        """A function to delete an obj from the current session"""
        if obj is not None:
            self.__session.delete(obj)
    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """A closer here"""
        self.reload(self.__session)
