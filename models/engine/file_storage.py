#!/usr/bin/python3
import json


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
        """set in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj.__dict__


    def save(self):
        """serializes __objects to the JSON file"""
        try:
            with open(FileStorage.__file_path, 'w') as f:  # 'w' vs 'a'?
                f.write(json.dumps(FileStorage.__objects))
        except:
            pass


    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.loads(f.read())
        except:
            pass
