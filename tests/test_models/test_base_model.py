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


    def test_id(self):          # marches
        self.assertEqual(str, type(BaseModel().id))

    def test_str(self):             # marches 
        b1 = BaseModel()
        self.assertEqual(type(str(b1)), str)
    
    def test_to_dict(self):     # marches
        b2 = BaseModel()
        self.assertTrue(dict, type(b2.to_dict))
    
    def test_save(self):           # marches
        b3 = BaseModel()
        update = b3.updated_at
        b3.save()
        self.assertNotEqual(update,b3.updated_at)
    