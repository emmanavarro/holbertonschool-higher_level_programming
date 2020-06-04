#!/usr/bin/python3
"""Student to JSON with filter module"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name,
        last_name and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary
        representation of a Student instance
        """

        if attrs is None:
            return self.__dict__
        dict = {}
        for element in attrs:
            if element in self.__dict__:
                dict[element] = self.__dict__[element]
        return dict
