#!/usr/bin/python3
"""
Module for class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that imports from BaseModel
    Attributes:
    email: email of User
    password: password of User
    first_name: first name of User
    last_name: last name of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
