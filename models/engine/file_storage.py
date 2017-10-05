#!/usr/bin/python3
"""FileStorage module that handles data storage"""

import models
import json
from datetime import datetime


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances

    Attributes:
       __file_path (str): path to the JSON file (ec: file.JSON)
       __objects (dict): empty but will store all objects by <class name>.id

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id

        Args:
            obj: an instance of the class to be saved to the data storage

        """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj
        # obj calls __str__() when print() is called

    def save(self):
        """serializes __objects to the JSON file"""
        # new dict that converts datetime object to str & adds __class__
        to_JSON_dict = {}
        try:
            with open(FileStorage.__file_path, 'w', encoding="UTF8") as f:
                for k, v in FileStorage.__objects.items():
                    # v is a class object
                    to_JSON_dict[k] = v.to_dict()
                json.dump(to_JSON_dict, f)
        except:  # error type TBD
            pass

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        attrs = {}
        time = "%Y-%m-%dT%H:%M:%S.%f"

        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF8") as f:
                for k, v in json.loads(f.read()).items():
                    for key, value in v.items():
                        '''construct a dictionary of attributes'''
                        attrs[key] = value
                    class_name = attrs['__class__']
                    del attrs['__class__']
                    '''recreate instance of the proper class'''
                    class_obj = models.classes[class_name](**attrs)
                    FileStorage.__objects.update({k: class_obj})

        except (ValueError, FileNotFoundError):
            pass
