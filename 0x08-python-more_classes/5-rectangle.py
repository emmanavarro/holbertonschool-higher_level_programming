#!/usr/bin/python3
""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get private instance width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get private instance height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns string representation of a Rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        string_sq = ""
        for i in range(self.height):
            string_sq += "#" * self.__width
            if i != self.__height - 1:
                string_sq += "\n"
        return string_sq

    def __repr__(self):
        """return a string representation of
        the rectangle to be able to recreate
        a new instance by
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints a messge when delete instance
        """
        print("Bye rectangle...")
