#!/usr/bin/python3
"""
Unittest for Base class
"""


import unittest
from models.base import Base


class BaseTests(unittest.TestCase):
    """Base test cases"""

    def setUp(self):
        """Method to set the start point"""
        Base._Base__nb_objects = 0

    def test00(self):
        """Test number 0 for base"""
        base0 = Base()
        base1 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)

    def test01(self):
        """Test number 1 for base"""
        base0 = Base("text")
        self.assertEqual(base0.id, "text")

if __name__ == '__main__':
    unittest.main()
