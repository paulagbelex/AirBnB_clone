#!/usr/bin/python3
"""
Contains a class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        """
        Function that initializes BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of BaseModel
        """
        first = type(self).__name__
        a = "[{}] ({}) {}".format(first, self.id, self.__dict__)
        return a

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        for key, value in new_dict.items():
            if key == "created_at":
                new_dict[key] = str(self.created_at.isoformat())
            if key == "updated_at":
                new_dict[key] = str(self.updated_at.isoformat())
        return new_dict
