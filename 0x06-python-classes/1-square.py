#!/usr/bin/python3
""" python3 -c 'print(__import__("my_module").Square.init)"""


class Square:
    """ python3 -c 'print(__import__("0-square").Square)'"""
    __size = 0
    def __init__(self, size=0):
        """Initialize class."""
        if size is not 0:
            self.__size = new_size 
        self.__size = size
