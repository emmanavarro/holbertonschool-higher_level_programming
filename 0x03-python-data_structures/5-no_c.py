#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for index in my_string:
        if index == 'c' or index == 'C':
            continue
        str += index
    return str
