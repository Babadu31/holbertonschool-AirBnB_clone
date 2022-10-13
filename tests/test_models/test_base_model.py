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


    def test_str(self):             # marches (changement venant de Chris)
        b1 = BaseModel()
        date_init = datetime.now()
        date_repr = repr(date_init)
        b1.created_at = b1.updated_at = date_init
        b1.id = "12102022"
        b_str = b1.__str__()

        self.assertIn("[BaseModel] (12102022)", b_str)
        self.assertIn("'id': '12102022'", b_str)
        self.assertIn("'created_at': "+ date_repr, b_str)
        self.assertIn("'updated_at': " + date_repr, b_str)


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
