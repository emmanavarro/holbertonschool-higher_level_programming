#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor that initialize a Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the arguments of square"""
        attr = ["id", "size", "x", "y"]
        if args:
            for index, item in enumerate(args):
                if index < 4:
                    setattr(self, attr[index], item)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
