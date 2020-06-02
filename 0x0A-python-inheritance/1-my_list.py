#!/usr/bin/python3
''' Creates a Class Mylist'''


class MyList(list):
    ''' Class MyList
        Args:
            List
    '''
    def print_sorted(self):
        ''' prints the list '''
        return (sorted(self))
