#!/usr/bin/python3
"""Console"""

import json
import cmd
import models
import shlex
import re
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

    def check_instance(self, class_name, inst_id, stored_objects):
        """
        Check if the instance exists & prints an error message if it doesn't.

        Args:
            class_name (str): class name of the instance
            inst_id (str): instance id
            stored_objects(dict): dictionary of instance "<class_name>.<id>"
                                  and instance objects
        Returns:
            "<class_name>.<id>" if the instance exists, False otherwise

        """
        '''get '<class_name>.id' to FileStorage.__objects key format'''
        instance = "{}.{}".format(class_name, inst_id)
        if instance not in stored_objects:
            """given id does not exist"""
            print("** no instance found **")
            instance = False
        return instance

    def basic_errs(self, args):
        """
        Check and print out basic errors.

        Args:
            args (list): list of parsed command arguments.

        Returns:
            True if it fits one of the error categories;
            False if not.
        """
        if len(args) == 0:
            '''if class name is missing'''
            print("** class name missing **")

        elif args[0] not in models.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            return True
        return False

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

        if self.basic_errs(args):
            '''check if instance exists'''
            instance = self.check_instance(args[0], args[1], stored_objects)
            if instance:
                print(stored_objects[instance])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id & save the change
        into the JSON file.
        """
        args = shlex.split(arg)
        stored_objects = models.storage.all()

        if self.basic_errs(args):
            '''check if instance exists'''
            instance = self.check_instance(args[0], args[1], stored_objects)
            if instance:
                """delete from FileStorage.__objects"""
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
                self.all(args[0], stored_objects)

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

        if self.basic_errs(args):
            if args[1] not in id_list:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                new_args = args[1:]
                self.update(args[0], new_args, stored_objects)

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
                self.get_func(args[0], args[1], stored_objects)
            else:
                print("** class doesn't exist **")
        else:
            super().default(arg)

    def get_func(self, class_name, arg, stored_objects):
        """
        Parse the argument from commandline functions;
        Invoke appropriate function & print corresponding error messages.

        Args:
            arg (string): <func_name>("arg_1". "arg_2",...)

        """
        find_func = re.match('([a-z]+)', arg)  # returns a matching object
        func_name = find_func.group()
        args = re.findall('"([^"]+)",?', arg)  # return a list of arguments

        if len(args) == 0:
            if func_name == "all":
                self.all(class_name, stored_objects)
            elif func_name == "count":
                self.count(class_name, stored_objects)
            else:
                print("** instance id missing **")

        elif len(args) == 1:
            if self.check_instance(class_name, args[0], stored_objects):
                if func_name == "show":
                    self.show(class_name, args[0], stored_objects)
                elif func_name == "destroy":
                    self.destroy(class_name, args[0], stored_objects)
                elif func_name == "update":
                    print("** attribute name missing **")

        elif len(args) == 2 and func_name == "update":
            print("** value missing **")

        elif len(args) == 3 and func_name == "update":
            if self.check_instance(class_name, args[0], stored_objects):
                self.update(class_name, args, stored_objects)


    def all(self, class_name, stored_objects):
        """
        Print out corresponding instances.

        Args:
            class_name (str): class the instance belongs to.
            stored_object (dict): dictionary of <class_name>.<id> and
                                  corresponding instance objects.

        """
        for k, v in stored_objects.items():
            if class_name in k:
                print(v)

    def count(self, class_name, stored_objects):
        """
        Count the number of instances corresponding to the class.

        Args:
            class_name (str): class the instance belongs to.
            stored_object (dict): dictionary of <class_name>.<id> and
                                  corresponding instance objects.

        """
        count = 0
        for k in stored_objects:
            inst_list = k.split('.')
            if inst_list[0] == class_name:
                count += 1
        print(count)

    def show(self, class_name, inst_id, stored_objects):
        """
        Print an instance based on class name and id.

        Args:
            class_name (str): class the instance belongs to.
            inst_id (str): id of the instance.
            stored_object (dict): dictionary of <class_name>.<id> and
                                  corresponding instance objects.

        """
        instance = "{}.{}".format(class_name, inst_id)
        if instance not in stored_objects:
            print("** no instance found **")
        else:
            print(stored_objects[instance])

    def destroy(self, class_name, inst_id, stored_objects):
        """
        Destroy an instance based on class name and id.

        Args:
            class_name (str): class the instance belongs to.
            inst_id (str): id of the instance.
            stored_object (dict): dictionary of <class_name>.<id> and
                                  corresponding instance objects.

        """
        instance = "{}.{}".format(class_name, inst_id)
        if instance not in stored_objects:
            print("** no instance found **")
        else:
            del stored_objects[instance]

    def update(self, class_name, args, stored_objects):
        """
        Update an instance based on ID, attribute name, & attribute value.

        Args:
            class_name (str): class the instance belongs to.
            args (list): list of args => ["<id>", "<attr_name>", "<attr_value>"]
            stored_object (dict): dictionary of <class_name>.<id> and
                                  corresponding instance objects.

        """
        id_list = [k.split(".")[1] for k in stored_objects]
        instance = "{}.{}".format(class_name, args[0])
        obj = stored_objects[instance]
        '''convert to the right attribute value type'''
        setattr(obj, args[1], args[2])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
