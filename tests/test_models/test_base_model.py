#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the BaseModel class.
    """
    def test_1(self):
        my_model = BaseModel()
        self.assertEqual(str(type(
            my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(issubclass(type(my_model), BaseModel))
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.name, "My First Model")
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        nme = "BaseModel"
        str_rep = "[{}] ({}) {}".format(nme, my_model.id, my_model.__dict__)
        self.assertEqual(my_model.__str__(), str_rep)
        my_model_json = my_model.to_dict()
        self.assertNotEqual(my_model.__dict__, my_model_json)
        self.assertEqual(type(my_model_json), dict)
        self.assertIn("__class__", my_model_json)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(my_model_json["created_at"], (
            my_model.created_at.isoformat()))
        self.assertEqual(my_model_json["updated_at"], (
            my_model.updated_at.isoformat()))
        self.assertEqual(my_model_json["name"], my_model.name)
        self.assertEqual(my_model_json["my_number"], my_model.my_number)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertRaises(TypeError, BaseModel, 1)
        self.assertRaises(TypeError, BaseModel.__init__)
        self.assertNotIsInstance(my_model_json, BaseModel)


if __name__ == '__main__':
    unittest.main()
