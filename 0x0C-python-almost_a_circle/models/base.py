#!/usr/bin/python3
""" new class called base """
import json


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation """
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))
