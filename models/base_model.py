#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

from datetime import datetime
import models  # why doesn't 'from models import storage' work?
# import var created in __init__ under models/
import uuid


class BaseModel:
    """Public instance attributes"""
    def __init__(self, *args, **kwargs):
        """initializing instance variables"""
        # set the default first
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        # if it's a new instance (not from dict reprsntion)
        # when nothing is passed to kwargs, it defaults to {}
        if not kwargs or kwargs is None:
            # store instance in dict to save to file later
            models.storage.new(self)

        else:
            # set given attribute from kwargs
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = self.to_datetime(v)
                self.__dict__[k] = v

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
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of"""
        dictionary_copy = self.__dict__.copy()
        """add class key and values to the copy"""
        dictionary_copy["__class__"] = type(self).__name__
        dictionary_copy["created_at"] = self.created_at.isoformat()
        dictionary_copy["updated_at"] = self.updated_at.isoformat()
        return dictionary_copy
