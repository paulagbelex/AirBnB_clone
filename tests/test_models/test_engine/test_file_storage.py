#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetimei

class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the FileStorage class.
    """
     def test_2(self):
        fs = FileStorage()
        self.assertEqual(type(fs._FileStorage__file_path), str)
        self.assertEqual(type(fs._FileStorage__objects), dict)
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertIsInstance(fs, FileStorage)
        self.assertEqual(type(fs.all()), dict)
        file_path = "file.json"
        try:
            file_path = FileStorage._FileStorage__file_path
        except:
            pass
        fs.save()
        self.assertTrue(os.path.exists(file_path))
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        storage.reload()
        obj = storage.all()
        for key, value in obj.items():
            can = value
            break
        self.assertTrue(can.__dict__ == my_model.__dict__)


if __name__ == '__main__':
    unittest.main()
