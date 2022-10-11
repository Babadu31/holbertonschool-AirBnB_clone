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
        b1 = BaseModel()
        self.assertTrue(dict, b1.to_dict())
    
    def test_save(self):           # marches
        b1 = BaseModel()
        update = b1.updated_at
        b1.save()
        self.assertNotEqual(update,b1.updated_at)
    