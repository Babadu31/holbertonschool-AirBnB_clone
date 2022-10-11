#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def TestSave(self):
        b = BaseModel()
        self.assertNotEqual(b.updated_at, b.created_at)
