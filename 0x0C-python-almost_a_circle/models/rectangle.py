#!/usr/bin/python3
"""Rectangle module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Args:
        Base (class): class that manage id
        attribute in all future classes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor to initialize"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """Print in stdo the Rectangle"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return string representation of Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the arguments of Rectangle"""
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for index, item in enumerate(args):
                if index < 5:
                    setattr(self, attr[index], item)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        attr = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attr}
