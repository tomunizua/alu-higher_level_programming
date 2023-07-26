#!/usr/bin/python3
"""

This module is for python

"""


class Square:
    """

    This module is for python

    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
