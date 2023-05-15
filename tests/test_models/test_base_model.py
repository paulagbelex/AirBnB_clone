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
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
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
        # Test when kwargs is not empty
        kwargs = {"id": "1234", "created_at": "2022-05-01T10:00:00.000000",
                "updated_at": "2022-05-02T10:00:00.000000"}
        b2 = BaseModel(**kwargs)
        self.assertEqual(b2.id, "1234")
        self.assertEqual(str(b2.created_at), "2022-05-01 10:00:00")
        self.assertEqual(str(b2.updated_at), "2022-05-02 10:00:00")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertFalse(my_model is my_new_model)


if __name__ == '__main__':
    unittest.main()
