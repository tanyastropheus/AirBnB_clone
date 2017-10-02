#!/usr/bin/python3
"""Console"""

import json
import cmd
import models
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    intro = """
                **************************************************************
                *                                                            *
                *                  'Welcome to HBNB!'                        *
                *                                                            *
                *              'Type help to list commands'                  *
                *                                                            *
                **************************************************************
            """

    prompt = "(hbnb) "

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

    def do_create(self, arg):
        """import withing method otherwise circular"""
        from models.base_model import BaseModel
        """Creates a new instance of BaseModel"""
        arg = arg.split()
        if arg[0] and len(arg) == 1:
             new_instance = BaseModel()
             print(new_instance.id)

        elif len(arg) == 0 or arg is None:
            """If the class name is missing"""
            print("** class name missing **")
        else:
            """If the class name doesn't exist"""
            print("** class doesn't exist **")
        """saves it (to the JSON file) """
        models.storage.save()

    def do_show(self, arg):





if __name__ == '__main__':
    HBNBCommand().cmdloop()
