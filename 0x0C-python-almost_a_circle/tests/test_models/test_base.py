#!/usr/bin/python3
"""
Unittest for Base class
"""


import unittest
import pep8
import json
import sys
import io
from models import base
from models.base import Base


class Test_Doc_Base(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class Test_Pep8_Base(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class BaseTests(unittest.TestCase):
    """Base test cases"""

    def setUp(self):
        """Method to set the start point"""
        Base._Base__nb_objects = 0

    def test00(self):
        """Test number 0 for base"""
        b_0 = Base()
        b_1 = Base()
        self.assertEqual(b_0.id, 1)
        self.assertEqual(b_1.id, 2)

    def test01(self):
        """Test number 1 for base"""
        b_0 = Base("text")
        self.assertEqual(b_0.id, "text")

    def test02(self):
        """Test number 2 for base"""
        b_0 = Base(24)
        self.assertEqual(b_0.id, 24)

    def test03(self):
        """Test number 3 for base"""
        b_0 = Base("test")
        self.assertEqual(b_0.id, "test")

    def test04(self):
        """Test number 4 for base"""
        b_0 = Base(-57)
        self.assertEqual(b_0.id, -57)

    def test05(self):
        """Test number 5 for base."""
        b_0 = Base(None)
        self.assertEqual(b_0.id, 1)

    def test06(self):
        """Test number 6 for base"""
        b_0 = Base({"test": "test"})
        self.assertEqual(b_0.id, {"test": "test"})

    def test07(self):
        """Test number 7 for base"""
        b_0 = Base([1, 2, 3])
        self.assertEqual(b_0.id, [1, 2, 3])

    def test08(self):
        """Test number 8 for base"""
        b_0 = Base(27.8)
        self.assertEqual(b_0.id, 27.8)

    def test09(self):
        """Test number 9 for base"""
        b_0 = Base()
        self.assertEqual(str(type(b_0)), "<class 'models.base.Base'>")
        self.assertEqual(b_0.__dict__, {"id": 1})

    def test10(self):
        """Test number 10 for base"""
        rect = Base.to_json_string(None)
        self.assertEqual(rect, "[]")
