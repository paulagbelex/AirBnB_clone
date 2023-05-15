#!/usr/bin/python3
"""
Contains a class BaseModel
"""

import uuid
from datetime import datetime
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
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.__dict__["created_at"] = (datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == "updated_at":
                    self.__dict__["updated_at"] = (datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            
    def __str__(self):
        """
        String representation of BaseModel
        """
        first = type(self).__name__
        a = "[{}] ({}) {}".format(first, self.id, self.__dict__)
        return a

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        for key, value in new_dict.items():
            if key == "created_at":
                new_dict[key] = value.isoformat()
            if key == "updated_at":
                new_dict[key] = value.isoformat()
        return new_dict
