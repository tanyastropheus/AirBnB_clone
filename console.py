#!/usr/bin/python3
"""Console"""

import json
import cmd
import models
from models.base_model import BaseModel
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
    
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


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
        """Creates a new instance of BaseModel"""

        arg = arg.split()
        if arg[0] and len(arg) == 1:
            # need to check against a list of given class names
            new_instance = BaseModel()
            print(new_instance.id)

        elif len(arg) == 0:
            """If the class name is missing"""
            print("** class name missing **")

        else:
            """If the class name doesn't exist"""
            print("** class doesn't exist **")

        """saves it (to the JSON file) """
        models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        arg = arg.split()
        """get FileStorage.__objects"""
        stored_objects = models.storage.all()
        """create a list of id from storage"""
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")

        elif len(arg) == 1:
            """missing id"""
            print("** instance id missing **")

        elif arg[1] not in id_list:
            """given id does not exist"""
            print("** no instance found **")

        else:
            """get '<class_name>.id' to FileStorage.__objects key format"""
            instance = "{}.{}".format(arg[0], arg[1])
            """search matching class object"""
            for k, v in stored_objects.items():
                if k == instance:
                    print(v)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id & save the change
        into the JSON file.
        """
        arg = arg.split()
        stored_objects = models.storage.all()
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(arg) == 0:
            '''if class name is missing'''
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")

        elif len(arg) == 1:
            print("** instance id missing **")

        elif arg[1] not in id_list:
            print("** no instance found **")

        else:
            instance = "{}.{}".format(arg[0], arg[1])
            """delete from FileStorage.__objects"""
            if instance in stored_objects.keys():
                del stored_objects[instance]
            """overwrite the new data to file.json"""
            models.storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
