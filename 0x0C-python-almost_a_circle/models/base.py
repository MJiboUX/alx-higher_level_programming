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

    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
