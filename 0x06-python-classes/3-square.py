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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the area of the current Square
        return: area
        """
        area = self.__size ** 2
        return area
