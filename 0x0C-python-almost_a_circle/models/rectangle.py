#!/usr/bin/python3
""" define class rectangle """
from .base import Base


class Rectangle(Base):
    """ import class base inherit """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @property
    def height(self):
        """ getter """
        return self.__height

    @property
    def x(self):
        """ getter """
        return self.__x

    @property
    def y(self):
        """ getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ define area """
        return self.__width * self.height

    def display(self):
        """ define display """
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """  overriding the __str__ method """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                  self.__x,
                                                                  self.__y,
                                                                  self.__width,
                                                                  self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """
            returns the dictionary
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
