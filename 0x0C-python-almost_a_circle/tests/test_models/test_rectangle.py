#!/usr/bin/python3
"""
Unittest for rectangle
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTests(unittest.TestCase):
    """Test cases for rectangle class"""

    def setUp(self):
        """Method to set the start point"""
        self.rec = Rectangle(10, 8, 4, 2, 1)

    def test00(self):
        """Test 0 for Rectangle"""
        rec = Rectangle(200, 64)
        self.assertEqual(isinstance(rec, Base), True)

    def test01(self):
        """Test 1 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(float("nan"), 1)
        self.assertEqual(
            "width must be an integer",
            str(error.exception))

    def test02(self):
        """Test 2 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(float("inf"), 1)
        self.assertEqual(
            "width must be an integer",
            str(error.exception))

    def test03(self):
        """Test 3 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(12)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(error.exception))

    def test04(self):
        """Test 4 for Rectangle"""
        rec = Rectangle(20, 4)
        self.assertEqual(rec.id, 4)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test05(self):
        """Test 5 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(error.exception))

    def test06(self):
        """Test 6 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(error.exception))

    def test07(self):
        """Test 7 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(22, "32")
        self.assertEqual(
            "height must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, 2, "3")
        self.assertEqual(
            "x must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, 2, 0, "epa")
        self.assertEqual(
            "y must be an integer",
            str(error.exception))

    def test08(self):
        """Test 8 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, 24.1)
        self.assertEqual(
            "height must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(9.12, 2)
        self.assertEqual(
            "width must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(12, 3, 6.7859)
        self.assertEqual(
            "x must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(12, 3, 0, 6123.5)
        self.assertEqual(
            "y must be an integer",
            str(error.exception))

    def test09(self):
        """Test 9 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, [])
        self.assertEqual(
            "height must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            r = Rectangle([1, 2, 3], 2)
        self.assertEqual(
            "width must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, 2, [[3, 4]])
        self.assertEqual(
            "x must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(12, 2, 0, ["test"])
        self.assertEqual(
            "y must be an integer",
            str(error.exception))

    def test10(self):
        """Test 10 for Rectangle"""
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, {})
        self.assertEqual(
            "height must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle({"3": 3, "2": 4, "1": 5}, 2)
        self.assertEqual(
            "width must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(10, 2, {"a": 1})
        self.assertEqual(
            "x must be an integer",
            str(error.exception))
        with self.assertRaises(TypeError) as error:
            rec = Rectangle(22, 2, 0, {"test": None})
        self.assertEqual(
            "y must be an integer",
            str(error.exception))

    def test12(self):
        """Test 11 for Rectangle"""
        with self.assertRaises(ValueError) as error:
            rec = Rectangle(1, -27)
        self.assertEqual(
            "height must be > 0",
            str(error.exception))
        with self.assertRaises(ValueError) as error:
            rec = Rectangle(-1, -23)
        self.assertEqual(
            "width must be > 0",
            str(error.exception))
        with self.assertRaises(ValueError) as error:
            rec = Rectangle(1, 2, -11)
        self.assertEqual(
            "x must be >= 0",
            str(error.exception))
        with self.assertRaises(ValueError) as error:
            rec = Rectangle(1, 2, 5, -167)
        self.assertEqual(
            "y must be >= 0",
            str(error.exception))

    def test13(self):
        """Test 13 for Rectangle"""
        with self.assertRaises(ValueError) as error:
            rec = Rectangle(7, 0)
        self.assertEqual(
            "height must be > 0",
            str(error.exception))
        with self.assertRaises(ValueError) as error:
            rec = Rectangle(0, 22)
        self.assertEqual(
            "width must be > 0",
            str(error.exception))
        rec = Rectangle(11, 21, 0, 0)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
