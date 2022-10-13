#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from models.engine import filestorage

class BaseModel:
    """
    Base class
    """

    def __init__(self, *args, **kwargs):
        if kwargs:                                               # ! trop de conditions                                                                 
                                                                 # dans le init pas sencé avoir autant de conditions
                                                                 # décomposer init en plusieurs fonctions
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            storage.new(self)


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
        models.storage.save()

    def to_dict(self):
        dictionary = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dictionary[key] = value
        return dictionary