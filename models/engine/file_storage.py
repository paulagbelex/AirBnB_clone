#!/usr/bin/python3
"""
Contains a class FileStorage
"""

import json
import os.path
from datetime import datetime


class FileStorage():
    """
    Class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        class_name = type(obj).__name__
        ide = obj.id
        FileStorage.__objects[class_name + '.' + ide] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        temp = {}
        tmp = FileStorage.__objects
        for key, value in tmp.items():
            if type(value) is not dict:
                value_1 = value.__dict__.copy()
                value_1['__class__'] = type(value).__name__
                obj.append(value)
                temp[key] = value_1
        if type(value) is not dict:
            for key_1, value_1 in temp.items():
                for key, v in value_1.items():
                    if key == 'created_at' and isinstance(v, (datetime, )):
                        value_1[key] = v.isoformat()
                    if key == 'updated_at' and isinstance(v, (datetime, )):
                        value_1[key] = v.isoformat()
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        if os.path.isfile(FileStorage.__file_path) is not True:
            return
        temp = {}
        f = open(FileStorage.__file_path, "r")
        data = json.loads(f.read())
        a = 1
        new = []
        b = 0
        for key_1, value_1 in data.items():
            temp[a] = value_1
            new.append(BaseModel(**temp[a]))
            FileStorage.__objects[key_1] = new[b]
            a = a + 1
            b = b + 1
