#!/usr/bin/python3
"""commentaire de module"""

import os
import json


class FileStorage:
    """Class to store data in json files"""

    __file_path = "file.json"
    __objects = {}
    
    """Public instance method"""

    def all(self):
        """return the dictionary __object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects the obj with key <obj classname>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file path: __file_path"""
        i_dict = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            json.dump(i_dict, f)

    def reload(self):
        """Deserialize the Json file __file_path to __objects, if it exists"""
        if os.path.exists(FileStorage.__file_path):
            path = FileStorage.__file_path
            with open(path, "r") as f :
                obj_dict = json.load(f)
                for k in obj_dict.values():
                    cls_name = k[__class__]
                    del k[__class__]
                    self.new(eval(cls_name)(**k))
