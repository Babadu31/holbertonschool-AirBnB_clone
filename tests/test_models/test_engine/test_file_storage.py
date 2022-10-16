#!/usr/bin/python3

import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestBase(unittest.TestCase):
    __file_path = "file.json"

    def test_all(self):
        base = BaseModel()
        all_storage = storage.all()
        self.assertIsNotNone(all_storage)
        self.assertEqual(all_storage, storage.all())
        self.assertIs(all_storage, storage.all())

    def test_new(self):
        all_storage = storage.all()
        User_ = User()
        User_.name = "Bill"
        user_id = User_.id
        storage.new(User_)
        self.assertIsNotNone(all_storage[User_.__class__.__name__ + "." + User_.id])

    def test_save(self):
        base = BaseModel()
        base.save
        with open(self.__file_path, "r") as f:
            dict_of_dict = json.load(f) 
        self.assertIsNotNone(dict_of_dict)

if __name__ == '__main__':
    unittest.main()