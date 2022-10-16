#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def TestSave(self):
        b0 = BaseModel()
        self.assertEqual(type(b0. id), str)
        self.assertEqual(type(b0.created_at), datetime)
        self.assertEqual(type(b0.updated_at), datetime)

    def test_id(self):
        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))

    def test_str(self):             # marches (changement venant de Chris)
        b1 = BaseModel()
        date_init = datetime.now()
        date_repr = repr(date_init)
        b1.created_at = b1.updated_at = date_init
        b1.id = "12102022"
        b_str = b1.__str__()

        self.assertIn("[BaseModel] (12102022)", b_str)
        self.assertIn("'id': '12102022'", b_str)
        self.assertIn("'created_at': " + date_repr, b_str)
        self.assertIn("'updated_at': " + date_repr, b_str)

#    def test_to_dict(self):     # marches mais beugé selon Taieb
#        b1 = BaseModel()
#        b2 = b1.to_dict()
#        self.assertTrue("{}", str(b2))

    def test_to_dict(self):     # marches
        b1 = BaseModel()
        b2 = b1.to_dict()
        self.assertIsNotNone(b2)
        self.assertEqual(dict, type(b2))

    def test_save(self):           # marches
        b1 = BaseModel()
        update1 = b1.updated_at
        b1.save()
        update2 = b1.updated_at
        self.assertNotEqual(update1,update2)

        if __name__ == "__main__":
            unittest.main()
