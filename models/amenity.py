#!/usr/bin/python3
"""Amenity Module"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public class attributes"""
    def __init__(self, *args, **kwargs):
        """create new Amenity"""
        super().__init__(self, *args, **kwargs)
