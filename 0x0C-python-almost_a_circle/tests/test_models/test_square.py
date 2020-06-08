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

    def test_01(self):
        """Test 01 for square"""
        sq = Square(12, 2, 1, 9)
        sq_dict = {'x': 2, 'size': 12, 'y': 1, 'id': 9}
        self.assertEqual(sq.to_dictionary(), sq_dict)
        self.assertEqual(sq.to_dictionary() is s_dict, False)


if __name__ == '__main__':
    unittest.main()
