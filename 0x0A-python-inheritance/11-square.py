#!/usr/bin/python3
"""Square Module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Constructor method for square
        Instantiation with size"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation"""

        return "[Square] {}/{}".format(self.__size, self.__size)
