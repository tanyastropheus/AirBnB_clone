#!/usr/bin/python3
"""Console"""

import json
import cmd
import models
import storage

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

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """import withing method otherwise circular"""
        from models.base_model import BaseModel
        """Creates a new instance of BaseModel"""
        if arg[0] and len(arg) == 1:
             new_instance = ["BaseModel"]
             print(new_instance.id)

        if len(arg) == 0 or arg is None:
            """If the class name is missing"""
            print("** class name missing **")
        else:
            """If the class name doesn't exist"""
            print("** class doesn't exist **")
        """saves it (to the JSON file) """
        storage.save()






if __name__ == '__main__':
    HBNBCommand().cmdloop()
