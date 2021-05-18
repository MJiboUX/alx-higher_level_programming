#!/usr/bin/python3
""" creates a square with size"""


class Square:
    """ creates a square with size """
    __size = 0
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
             raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """define area"""
        A = self.__size * self.__size
        return (A)
    @property
    def size(self):
          """Gets def"""
          return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
