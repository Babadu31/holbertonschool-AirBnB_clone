#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    
    def test_attributes(self):
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

    def test_email(self):
        u = User()
        self.assertEqual(str, type(User.email))
        self.assertTrue(hasattr(u, "email"))

    def test_password(self):
        u = User()
        self.assertEqual(str, type(User.password))
        self.assertTrue(hasattr(u, "password"))

    def test_first_name(self):
        u = User()
        self.assertEqual(str, type(User.first_name))
        self.assertTrue(hasattr(u, "first_name"))

    def test_last_name(self):
        u = User()
        self.assertEqual(str, type(User.last_name))
        self.assertTrue(hasattr(u, "last_name"))

if __name__ == '__main__':
    unittest.main()