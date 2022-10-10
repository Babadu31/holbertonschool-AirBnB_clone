#!/usr/bin/python3
"""
command intepreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


class AirBnBCommand(cmd.Cmd):
    """
    interpreter class from cmd
    """
    prompt = '(AirBnB)'
    classes_list = ["BaseModel", "User", "State", "City", "Place"]

    def EOF(self, line):
        