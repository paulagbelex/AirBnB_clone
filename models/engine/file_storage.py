#!/usr/bin/python3
"""
Contains a class FileStorage
"""

import json
import os.path
import datetime


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
        a = 1
        old_storage = {}
        for key, value in FileStorage.__objects.items():
            if type(value) is not dict:
                old_storage[a] = value
            a = a + 1
        obj = []
        for key, value in tmp.items():
            if type(value) is not dict:
                value_1 = value.__dict__.copy()
                obj.append(value)
                temp[key] = value_1
            else:
                temp[key] = value
        a = 0
        if type(value) is not dict:
            for key_1, value_1 in temp.items():
                for key in value_1:
                    if key == 'created_at':
                        value_1[key] = str(obj[a].created_at.isoformat())
                    if key == 'updated_at':
                        value_1[key] = str(obj[a].updated_at.isoformat())
                value_1['__class__'] = type(obj[a]).__name__
                a = a + 1
        else:
            val = temp['updated_at']
            temp['updated_at'] = str(val.isoformat())
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(temp, json_file)
        """
        for key_1, value_1 in old_storage.items():
            for key, value in value_1.items():
                if key == 'created_at':
                    value_1[key] = datetime.datetime.strptime
                    (value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    value_1[key] = datetime.datetime.strptime
                    (value, '%Y-%m-%dT%H:%M:%S.%f')
        for key_1, value_1 in old_storage.items():
            for key, value in value_1.items():
                if key == '__class__':
                    del value_1[key]
                    break
        """
        a = 1
        for key, value in FileStorage.__objects.items():
            FileStorage.__objects[key] = old_storage[a]
            a = a + 1

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
