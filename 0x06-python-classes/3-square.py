#!/usr/bin/python3
""" defines a square with size"""


class Square:
    """ Square Class
    
        Attributes:
            size (int): size of square
    """
    __size = 0

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Initialize method """
        A = self.__size * self.__size
        return (A)
