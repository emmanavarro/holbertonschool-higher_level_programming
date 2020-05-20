#!/usr/bin/python3
""" Creates a class Square that defines a square """


class Square():
    """ Square class with two private atributes """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ is a constructor of square class
        Args:
            size (int): size of square
            position (tuple): position of Square
        """
        self.size = size
        try:
            self.position = position
        except TypeError as err:
            print(err)

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

    @property
    def position(self):
        """ Get method
        return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculates the area of the current Square
        return: area
        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """ print a square
        """
        if self.__size:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.__size))
        else:
            print()
