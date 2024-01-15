#!/usr/bin/python3
"""Module bases class"""


class Base:
    """A representation of the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constractor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
