#!/usr/bin/python3
"""
Contains a class BaseModel
"""

import uuid
import datetime
from models import storage


class BaseModel():
    """
    Class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Function that initializes BaseModel
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
            self.created_at = datetime.datetime.strptime(self.(
                created_at, '%Y-%m-%dT%H:%M:%S.%f'))
            self.updated_at = datetime.datetime.strptime(self.(
                updated_at, '%Y-%m-%dT%H:%M:%S.%f'))

    def __str__(self):
        """
        String representation of BaseModel
        """
        first = type(self).__name__
        a = "[{}] ({}) {}".format(first, self.id, self.__dict__)
        return a

    def save(self):
        """
        Function to update the public instance
        attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.datetime.today()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        self.__dict__['__class__'] = type(self).__name__
        self.created_at = str(self.created_at.isoformat())
        self.updated_at = str(self.updated_at.isoformat())
        return self.__dict__
