#!/usr/bin/python3
"""
Unittest for Square
"""


import unittest
import pep8
from models.square import Square
from models import square


class Test_Doc_Square(unittest.TestCase):
    """ checking for documentation """
    def test_module_doc(self):
        """ checking for module documentation """
        self.assertTrue(len(square.__doc__) > 0)

    def test_class_doc(self):
        """ checking for class documentation """
        self.assertTrue(len(Square.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method documentation """
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)


class Test_Pep8_Square(unittest.TestCase):
    """ checking for pep8 validation """
    def test_pep8(self):
        """ testing square and test_square for pep8 """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/square.py'
        file2 = 'tests/test_models/test_square.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


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
        self.assertEqual(sq.to_dictionary() is sq_dict, False)

    def test_x(self):
        """test x """

        self.assertEqual(self.sq.x, 6)

    def test_y(self):
        """test y """

        self.assertEqual(self.sq.y, 10)

    def test_negative(self):
        """test negative size"""

        with self.assertRaises(ValueError):
            ob = Square(-1)

    def test_sizeSetter(self):
        """Size is not a integer"""

        self.assertRaises(TypeError, Square, "Hello")
