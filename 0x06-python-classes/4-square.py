#!/usr/bin/python3
""" Creates a class Square that defines a square """


class Square:
    """ Square class with one privete atribute """
    def __init__(self, size=0):
        """__init__ is a constructor of square class
        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """ Get method
        return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the area of the current Square
        return: area
        """
        area = self.__size ** 2
        return area
