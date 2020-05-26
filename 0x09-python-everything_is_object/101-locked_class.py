#!/usr/bin/python3
"""class LockedClass with no
class or object attribute
"""


class LockedClass:
    """Class that prevents different instance"""
    __slots__ = ['first_name']
