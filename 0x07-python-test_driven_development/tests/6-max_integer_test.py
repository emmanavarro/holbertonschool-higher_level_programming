#!/usr/bin/python3
"""
    Unittest
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Testing function
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-5, -30, -15, -23]), -5)
        self.assertEqual(max_integer([3.4, -2.1]), 3.4)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([89]), 89)
        self.assertEqual(max_integer([1.3, 23, 10, 90.1, 90.2]), 90.2)

if __name__ == '__main__':
    unittest.main()
