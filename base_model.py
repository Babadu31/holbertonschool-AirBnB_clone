#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Base class
    """
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid4())


    def __str__(self):
        """
        string
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        un truc pértinent
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """"
        un second truc pertinent
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (dict_obj)
