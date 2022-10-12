#!/usr/bin/python3
"""
command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    console
    """
    prompt = "(hbnb)"

    def emptyline(self):            # à vérifier 
        pass

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        return True

    def help_quit(self):
        print("Quit command used to exit the program")
        print()

    def help_EOF(self):
        print("EOF command used to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()