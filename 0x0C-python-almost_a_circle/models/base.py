#!/usr/bin/python3
""" new class called base """


class Base:
    """ define Base with id """

    __nb_objects = 0

    def __init__(self, id=None):
        """ method initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
