#!/usr/bin/python3
"""
command interpreter
"""

import cmd
from models.base_model import BaseModel
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    console
    """
    prompt = "(hbnb)"
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
        ]

    def emptyline(self):       
        pass

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("Quit command used to exit the program")
        print()

    def help_EOF(self):
        print("EOF command used to exit the program")
        print()

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_create = eval(arg)()
            print(new_create.id)

    def do_show(self, arg):
        args = arg.split(" ")
        if arg == '':
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2 :
            print("** instance id missing **")
        else:
            id_instance = storage.all()
            string = "{}.{}".format(args[0], args[1])
            if string not in id_instance:
                print("** no instance found **")
            else:
                print("{}".format(id_instance[string]))

    def do_destroy(self, arg):
        args = arg.split(" ")
        if arg == '':
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id_instance = storage.all()
            string = "{}.{}".format(args[0], args[1])
            if string not in id_instance:
                print("** no instance found **")
            else:
                del (id_instance[string])
                storage.save()

    def do_all(self, arg):
        list = []
        all_directory = storage.all()
        if arg == "":
            for keys, values in all_directory.items():
                list.append(str(values))
            print(list)
        elif arg in self.__classes:
            for keys, values in all_directory.items():
                if values.__class__.__name__ == arg:
                    list.append(str(values))
            print(list)
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()