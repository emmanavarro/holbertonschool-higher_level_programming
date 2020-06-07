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
        self.sq = Square(10, 6, 10)

    def test00(self):
        """Test 00 for square"""
        self.assertEqual(self.sq.size, 10)


if __name__ == '__main__':
    unittest.main()
