#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
 
    def TestSave(self):         # ne marches pas 
        b0 = BaseModel()
        self.assertEqual(type(b0. id), str)
        self.assertEqual(type(b0.created_at), datetime)
        self.assertEqual(type(b0.updated_at), datetime)

    def test_id(self):
        b1 = BaseModel()          # marches
        self.assertEqual(str, type(b1.id))


    def test_str(self):             # marches 
        b1 = BaseModel()
        self.assertEqual(str(b1),  b1.__str__())

    def test_to_dict(self):     # marches
        b1 = BaseModel()
        b2 = b1.to_dict()
        self.assertIsNotNone(b2["__class__"])
        self.assertEqual(str, type(b2["updated_at"]))
        self.assertEqual(str, type(b2["created_at"]))

    def test_save(self):           # marches
        b1 = BaseModel()
        update1 = b1.updated_at
        b1.save()
        update2 = b1.updated_at
        self.assertNotEqual(update1,update2)
    
if __name__ == "__main__":
    unittest.main()
