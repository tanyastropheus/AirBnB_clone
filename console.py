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

    def check_instance(self, class_name, inst_id, stored_objects):
        """
        check if the instance exists & prints an error message if it doesn't.

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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        """get FileStorage.__objects"""
        stored_objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in models.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            """missing id"""
            print("** instance id missing **")

        else:
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
        id_list = [k.split(".")[1] for k in stored_objects.keys()]

        if len(args) == 0:
            '''if class name is missing'''
            print("** class name missing **")

        elif args[0] not in models.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
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
                self.all(stored_objects, args)

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
                    self.all(stored_objects, args)
                elif args[1] == 'count()':
                    self.count(stored_objects, args)
                else:
                    '''retreive function name'''
                    match_fname = re.match('([a-z]+)', args[1])
                    if match_fname.group() == 'show':
                        '''call show()'''
                        self.show(stored_objects, args[0], args[1])
                    elif match_fname.group() == 'destroy':
                        '''call destroy'''
                        self.destroy(stored_objects, args[0], args[1])
                    elif match_fname.group() == 'update':
                        self.update(stored_objects, args[0], args[1])
        else:
            super().default(arg)

    def all(self, instance_dict, args):
        """print out corresponding instances"""
        for k, v in instance_dict.items():
            if args[0] in k:
                print(v)

    def count(self, instance_dict, args):
        """count the number of instances corresponding to the class"""
        count = 0
        for k in instance_dict:
            inst_list = k.split('.')
            if inst_list[0] == args[0]:
                count += 1
        print(count)

    def show(self, instance_dict, class_name, arg):
        """retrieve the an instance based on ID"""
        '''get id'''

        inst_id = re.search('\("(.+)"\)', arg)

        '''if <id> exists'''
        if inst_id:
            '''need to turn id into str for formatting'''
            instance = "{}.{}".format(class_name, inst_id.group(1))
            if instance not in instance_dict:
                print("** no instance found **")
            else:
                print(instance_dict[instance])

        else:
            print("** instance id missing **")

    def destroy(self, instance_dict, class_name, arg):
        """destroy an instance based on ID"""
        '''get id'''

        inst_id = re.search('\("(.+)"\)', arg)

        '''if <id> exists'''
        if inst_id:
            '''need to turn id into str for formatting'''
            instance = "{}.{}".format(class_name, inst_id.group(1))
            if instance not in instance_dict:
                print("** no instance found **")
            else:
                del instance_dict[instance]

        else:
            print("** instance id missing **")

    def update(self, instance_dict, class_name, arg):
        """update an instance based on ID, attribute name, & attribute value"""
        '''get id'''
        args = re.findall('"([^"]+)",?', arg)
        id_list = [k.split(".")[1] for k in instance_dict]

        if class_name not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 0:
            print("** instance id missing **")
        elif args[0] not in id_list:
            print("** no instance found **")
        elif len(args) == 1:
            print("** attribute name missing **")
        elif len(args) == 2:
            print("** value missing **")
        else:
            instance = "{}.{}".format(class_name, args[0])
            obj = instance_dict[instance]
            '''convert to the right attribute value type'''
            setattr(obj, args[1], args[2])
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
