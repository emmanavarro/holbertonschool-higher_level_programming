#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """Class MyInt"""

    def __init__(self, value):
        """Constructor method"""

        if isinstance(value, int):
            self.__int = value

    def __ne__(self, value):
        """Method for the != conditional"""

        return True

    def __eq__(self, value):
        """Method for the == conditional"""

        return False
