#!/usr/bin/python3
"""Console"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = """
                **************************************************************
                *                                                            *
                *                  'Welcome to HBNBC!'                       *
                *                                                            *
                *              'Type help to list commands'                  *
                *                                                            *
                **************************************************************
            """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """
        overloads the emptyline method (that would revert back to the last command);
        This will make console display prompt again.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
