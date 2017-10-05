#!/usr/bin/python3
"""User Module"""


from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """create new user"""
        super().__init__(self, *args, **kwargs)
