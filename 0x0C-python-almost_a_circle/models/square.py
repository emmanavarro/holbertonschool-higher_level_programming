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
