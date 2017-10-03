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
        overloads the emptyline method (that would revert back to the last
        command);
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
        """Prints the string representation of an instance"""
        from models.engine.file_storage import FileStorage

        arg = arg.split()
        class_list = ['BaseModel']
        """get FileStorage.__objects"""
        stored_objects = models.storage.all()
        """create a list of id from storage"""
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in class_list:
            print("** class doesn't exist **")

        elif len(arg) == 1:
            """missing id"""
            print("** instance id missing **")

        elif arg[1] not in id_list:
            """given id does not exist"""
            print("** instance id missing **")

        else:
            """get '<class_name>.id' to match key in FileStorage.__objects"""
            instance = "{}.{}".format(arg[0], arg[1])
            """find matching class object"""
            for k, v in stored_objects.items():
                if k == instance:
                    print(v)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
