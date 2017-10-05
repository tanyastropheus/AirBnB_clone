#!/usr/bin/python3
"""State Module"""


from models.base_model import BaseModel


class State(BaseModel):
    """Public class attributes"""
    def __init__(self, *args, **kwargs):
        """create new state"""
        super().__init__(self, *args, **kwargs)
