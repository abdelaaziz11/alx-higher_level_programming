#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square
    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        """defines size of square
        Args:
            size: size of square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Calculates the area of square
        Returns: the current
        """
        return self.__size ** 2
