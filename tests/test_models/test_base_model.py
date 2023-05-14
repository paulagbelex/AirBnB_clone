import unittest
import datetime
import uuid

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        # Test when kwargs is empty
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime.datetime)
        self.assertIsInstance(b1.updated_at, datetime.datetime)

        # Test when kwargs is not empty
        kwargs = {"id": "1234", "created_at": "2022-05-01T10:00:00.000000",
                "updated_at": "2022-05-02T10:00:00.000000"}
        b2 = BaseModel(**kwargs)
        self.assertEqual(b2.id, "1234")
        self.assertEqual(str(b2.created_at), "2022-05-01 10:00:00")
        self.assertEqual(str(b2.updated_at), "2022-05-02 10:00:00")

    def test_id(self):
        b = BaseModel()
        self.assertIsInstance(b.id, str)
        self.assertIsNotNone(b.id)

    def test_to_dict(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["__class__"], "BaseModel")
    def test_save(self):
        b = BaseModel()
        original_updated_at = b.updated_at
        with patch('datetime.datetime') as mock_date:
            mock_date.today.return_value = datetime.datetime(2022, 5, 1)
            b.save()
            self.assertNotEqual(original_updated_at, b.updated_at)
            self.assertEqual(b.updated_at, datetime.datetime(2022, 5, 1))


if __name__ == '__main__':
    unittest.main()
