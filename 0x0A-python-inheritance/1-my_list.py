#!/usr/bin/python3
"""
module for MyList
"""


class MyList(list):
    """ Mylist """

    def print_sorted(self):
        """ prints the list sorted """
        print(sorted(self))
