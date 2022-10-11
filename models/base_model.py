#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel :
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dttime_ob = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dttime_ob)
                elif key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)
    
    def __str__(self):
        """
        string
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        dict
        """
        dict = {}
        dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
     