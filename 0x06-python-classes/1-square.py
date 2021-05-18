#!/usr/bin/python3
""" python3 -c 'print(__import__("my_module").Square.init)"""


class Square:
    """Square \n
    Attributes:
    size: square size
    """"""
    
    def __init__(self, size):
        """Initialize class"""
        self.__size = size
