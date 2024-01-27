#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            for myKey, myValue in kwargs.items():
                if myKey == 'updated_at' or myKey == 'created_at':
                    myValue = datetime.strptime(kwargs[myKey],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                if myKey != '__class__':
                    setattr(self, myKey, myValue)
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
