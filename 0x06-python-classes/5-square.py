#!/usr/bin/python3
""" defines a square with size"""


class Square:
    __size = 0
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
             raise ValueError('size must be >= 0')
        self.__size = size
        
    def area(self):
        A = self.__size * self.__size
        return (A)
      
    @property
    def size(self):
        """getter def"""
        return self.__size
      
    @property
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif size < 0:
             raise ValueError('size must be >= 0')
        self.__size = size
