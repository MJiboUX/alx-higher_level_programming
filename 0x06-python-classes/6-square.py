#!/usr/bin/python3
class Square:
    __size = 0
    __position = (0,0)
    def __init__(self, size=0, position=(0, 0)):
        """Initialize class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
        
    @property
    def position(self):
        """getter def"""
        return self.__position

    def area(self):
        """Square area."""
        return (self.__size * self.__size)

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
        
    @position.setter
    def position(self, value):
        """setter def"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
            
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
