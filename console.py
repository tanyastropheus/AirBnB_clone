#!/usr/bin/python3
"""Console"""

import json
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """creates a console for testing AirBnB setup"""
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
        """Creates a new instance of BaseModel"""

        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")

        elif args[0] in models.classes:
            new_instance = models.classes[args[0]]()
            print(new_instance.id)
            """saves it (to the JSON file) """
            models.storage.save()

        else:
            print("** class doesn't exist **")


    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        """get FileStorage.__objects"""
        stored_objects = models.storage.all()
        """create a list of id from storage"""
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in models.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            """missing id"""
            print("** instance id missing **")

        else:
            """get '<class_name>.id' to FileStorage.__objects key format"""
            instance = "{}.{}".format(args[0], args[1])
            if instance not in stored_objects:
                """given id does not exist"""
                print("** no instance found **")

            else:
                """search matching class object"""
                for k, v in stored_objects.items():
                    if k == instance:
                        print(v)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id & save the change
        into the JSON file.
        """
        args = shlex.split(args)
        stored_objects = models.storage.all()
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(args) == 0:
            '''if class name is missing'''
            print("** class name missing **")

        elif args[0] not in models.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            """get '<class_name>.id' to FileStorage.__objects key format"""
            instance = "{}.{}".format(args[0], arg[1])
            if instance not in stored_objects:
                """given id does not exist"""
                print("** no instance found **")
            else:
                """delete from FileStorage.__objects"""
                if instance in stored_objects.keys():
                    del stored_objects[instance]
                    """overwrite the new data to file.json"""
                models.storage.save()

    def do_all(self, arg):
        '''
        Print all string representation of all instances
        based on the class name
        '''
        args = shlex.split(arg)
        stored_objects = models.storage.all()

        if len(args) == 1:  # if given class name
            if args[0] in models.classes:  # if class name exists
                for k, v in stored_objects.items():
                    '''print out corresponding instances'''
                    if args[0] in k:
                        print(v)
            else:
                print("** class doesn't exist **")

        elif len(args) == 0:  # if not specifying class name
            '''print out all instances'''
            for v in stored_objects.values():
                print(v)

    def do_update(self, arg):
        '''update an instance & save the change to the JSON file'''
        args = shlex.split(arg)
        stored_objects = models.storage.all()
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] not in id_list:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance = "{}.{}".format(args[0], args[1])
            obj = stored_objects[instance]
            '''convert to the right attribute value type'''
            setattr(obj, args[2], args[3])
            models.storage.save()

    def default(self, arg):
        """
        add the following functionalities to the commandline:

        <class name>.all(): retrieve all instances of a class
        <class name>.count(): retrieve the number of instances of a class
        <class name>.show(<id>): retrieve the an instance based on its ID
        <class name>.destroy(<id>): destroy an instance based on its ID
        <class name>.update(<id>, <attribute name>, <attribute value>): update
        an instance based on its ID
        <class name>.update(<id>, <dictionary representation>): update an
        instance based on its ID with a dictionary

        """
        args = arg.split('.')
        stored_objects = models.storage.all()
        if len(args) == 2:
            if args[0] in models.classes:
                if args[1] == 'all()':
                    for k, v in stored_objects.items():
                        if args[0] in k:
                            print(v)
                elif args[1] == 'count()':
                    print(self.count(stored_objects, args))
                else:
                    print("**command not found**")
            else:
                print("**class doesn't exist**")
        else:
            super().default(arg)

    def count(self, instance_dict, args):
        count = 0
        for k in instance_dict:
            inst_list = k.split('.')
            if inst_list[0] == args[0]:
                count += 1
        return count
'''
    def show(self, arg):
        args = arg,split('.')
'''

if __name__ == '__main__':
    HBNBCommand().cmdloop()
