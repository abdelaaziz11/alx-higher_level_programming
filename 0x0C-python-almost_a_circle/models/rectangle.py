#!/usr/bin/python3
"""Module Rectangle class"""
from models.base import Base


class Rectangle:
    """A representation of the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init def"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """with of rectangle"""
        return self.__width

    @width.setter
    def __width(self, value):
        self.__width = value

    @property
    def height(self):
        """hieght of rectangle"""
        return self.__height

    @height.setter
    def __height(self, value):
        self.__height = value

    @property
    def x(self):
        """x of rectangle"""
        return self.__x

    @x.setter
    def __x(self, value):
        self.__x = value

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @y.setter
    def __y(self, value):
        self.__y = value
