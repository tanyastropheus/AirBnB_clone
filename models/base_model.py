#!/usr/bin/python3
from datetime import datetime, strftime
import uuid
"""defines all common attributes/methods for other classes"""


class BaseModel:
    """Public instance attributes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        """assign with the current datetime when an instance is created"""
        self.created_at = datetime.created_at()
	"""will be updated every time you change your object"""
        self.updated_at = datetime.updated_at()

    def __str__(self):
        """print class name, id, dict"""
        print([<class name>] (<self.id>) <self.__dict__>)


