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

    def emptyLine(self):            # à vérifier 
        pass

    def do_quit(self, arg):
        raise SystemExit

    def EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("Quit command used to exit the program")
        print()

    def help_EOF(self):
        print("EOF command used to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()