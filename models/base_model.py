#!/usr/bin/python3
from datetime import datetime
from models import storage # import var created in __init__ under models/
import uuid

"""defines all common attributes/methods for other classes"""


class BaseModel:
    """Public instance attributes"""
    def __init__(self, *args, **kwargs):
        if kwargs is None:  # if it's a new instance (not from dict reprsntion)
            storage.new()  # store instance in dictionary to save to file later

        else:
            print("test: ", kwargs.items())

            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = self.to_datetime(v)
                setattr(self, k, v)

            if 'id' not in self.__dict__:
                self.id = str(uuid.uuid4())
            if 'created_at' not in self.__dict__:
                self.created_at = datetime.now()
            if 'updated_at' not in self.__dict__:
                self.updated_at = self.created_at

    def to_datetime(self, string):
        """convert datetime string to datetime object"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        return datetime.strptime(string, time)

    def __str__(self):
        """print class name, id, dict"""
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of"""
        dictionary_copy = self.__dict__.copy()
        """add class key and values to the copy"""
        dictionary_copy["__class__"] = type(self).__name__
        dictionary_copy["created_at"] = self.created_at.isoformat()
        dictionary_copy["updated_at"] = self.updated_at.isoformat()
        return dictionary_copy
