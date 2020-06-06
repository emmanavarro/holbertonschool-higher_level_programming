#!/usr/bin/python3
"""Base module
"""


class Base:
    """Base class that manage id attribute in all future
    classes and to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method to initialize a Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
