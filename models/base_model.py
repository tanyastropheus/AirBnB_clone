#!/usr/bin/python3
from datetime import datetime
import uuid


"""defines all common attributes/methods for other classes"""


class BaseModel:
    """Public instance attributes"""
    def __init__(self, *args, **kwargs):
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            """assign with the current datetime when an instance is created"""
            self.created_at = datetime.now()
            """will be updated every time you change your object"""
            self.updated_at = self.created_at

    def __str__(self):
        """print class name, id, dict"""
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of"""
        dictionary_copy = self.__dict__.copy()
        """add class key and values to the copy"""
        dictionary_copy["__class__"] = type(self).__name__
        dictionary_copy["created_at"] = self.created_at.isoformat()
        dictionary_copy["updated_at"] = self.updated_at.isoformat()
        return dictionary_copy
