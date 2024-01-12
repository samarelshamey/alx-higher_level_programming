#!/usr/bin/python3
"""module for base class"""
from json import dumps, loads


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_objs = [x.to_dictionary() for x in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_list = f.read()
                python_list = cls.from_json_string(json_list)
                return [cls.create(**obj) for obj in python_list]
        except FileNotFoundError:
            return []
