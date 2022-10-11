#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base class
    """
    def __init__(self):
        self.id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """
        string
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        updated_at = datetime.now()

    def to_dict(self):
        dict_obj = self.__dict__
        dict_obj["__class__"] = self.__class__.__name__
        self.created_at = created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (dict_obj)