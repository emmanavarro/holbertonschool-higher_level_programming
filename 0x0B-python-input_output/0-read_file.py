#!/usr/bin/python3
"""Read text file module
"""


def read_file(filename=""):
    """
    Write a function that reads a text file
    (UTF8) and prints it to stdout.
    """

    with open('my_file_0.txt', mode='r', encoding='utf-8') as my_file:
        line = my_file.read()
        print(line, end='')
