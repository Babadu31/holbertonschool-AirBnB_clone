#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    """
    defines base model attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
        create à new instance and save the info
        """
        if kwargs:                                                                                                   
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            storage.new(self)


    def __str__(self):
        """
        Change output to a specific format
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        un truc pértinent
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dictionary[key] = value
        return dictionary
        