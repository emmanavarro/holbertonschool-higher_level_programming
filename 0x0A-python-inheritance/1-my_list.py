#!/usr/bin/python3
''' Class Mylist '''


class MyList(list):
    ''' Class that inherits from list '''
    def print_sorted(self):
        ''' prints the list '''
        return (sorted(self))
