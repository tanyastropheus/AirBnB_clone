#!/usr/bin/python3
"""Review Module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """create new Review"""
        super().__init__(self, *args, **kwargs)
