#!/usr/bin/python3
""" defines a square with size"""


class Square:
    """ defines a square with size  
        Attributes:
            size (int): size of square
    """
    __size = 0
    def __init__(self, size=0):
        """Initialize square    
            Args:
                size (int): integer for square size
            Raises:
                TypeError: if size is not int
                ValueError: size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
             raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """ square area """
        A = self.__size * self.__size
        return (A)
    @property
    def size(self):
          """getter def"""
          return self.__size
    @size.setter
    def size(self, value):
        """setter def"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
