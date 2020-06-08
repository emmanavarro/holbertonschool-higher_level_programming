#!/usr/bin/python3
"""Base module"""


import json


class Base:
    """Base class that manage id attribute in all future
    classes and to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method to initialize Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries is []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        newfile = "{}.json".format(cls.__name__)
