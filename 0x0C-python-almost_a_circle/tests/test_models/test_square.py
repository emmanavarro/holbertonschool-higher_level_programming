#!/usr/bin/python3
"""
Unittest for Square
"""


import unittest
from models.square import Square


class SquareTests(unittest.TestCase):
    """Test cases for square class"""

    def setUp(self):
        """Method to set the start point"""
        self.sq = Square(1, 5, 4)


if __name__ == '__main__':
    unittest.main()
