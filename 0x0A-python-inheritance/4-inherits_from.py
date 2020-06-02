#!/usr/bin/python3
''' Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
'''


def inherits_from(obj, a_class):
    ''' Args:
        obj: class object
        a_class: class
    '''

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
