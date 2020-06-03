#!/usr/bin/python3
"""Create object from a JSON file module"""


import json


def load_from_json_file(filename):
    """function that writes an Object to a text
    file, using a JSON representation
    """

    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.loads(my_file.read())
