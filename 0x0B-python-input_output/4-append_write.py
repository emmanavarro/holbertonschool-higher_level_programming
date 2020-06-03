#!/usr/bin/python3
'''Append to a file module'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a
    text file and returns the number of characters added
    '''

    with open(filename, mode='a', encoding='utf-8') as my_file:
        return my_file.write(text)
