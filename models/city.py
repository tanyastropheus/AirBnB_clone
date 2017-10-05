#!/usr/bin/python3
"""City Module"""


from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """create new city"""
        super().__init__(self, *args, **kwargs)
