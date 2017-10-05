#!/usr/bin/python3
"""Place Module"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Public class attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ["", ""]

    def __setattr__(self, name, value):
        if name == "number_rooms" and type(value) == str:
            self.number_rooms = int(value)
        elif name == "number_bathrooms" and type(value) == str:
            self.number_bathrooms = int(value)
        elif name  == "max_guest" and type(value) == str:
            self.max_guest = int(value)
        elif name == "price_by_night" and type(value) == str:
            self.price_by_night = int(value) 
        elif name == "latitude" and type(value) == str:
            self.latitude = float(value)
        elif name == "longitude" and type(value) == str:
            self.longitude = float(value)
        else:
            super().__setattr__(name, value)
