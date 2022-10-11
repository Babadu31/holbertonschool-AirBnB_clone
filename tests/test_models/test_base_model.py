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

    @unittest.skip("Waiting for taieb")
    def test_to_dict(self):     # marches
        b1 = BaseModel()
        b2 = b1.to_dict()
        self.assertTrue("{}", str(b2))

    def test_save(self):           # marches
        b1 = BaseModel()
        update = b1.updated_at
        b1.save()
        self.assertNotEqual(update,b1.updated_at)
    
if __name__ == "__main__":
    unittest.main()
