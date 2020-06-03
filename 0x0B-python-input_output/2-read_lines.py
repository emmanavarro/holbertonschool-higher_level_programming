#!/usr/bin/python3
""" In this module it create a function
that read n line of a file
"""


def read_line(filename="", nb_line=0):
    """function that reads n line of a
    text file and prints it to stdout
    """

    with open(filename, mode='r', encoding='utf-8') as myFile:
        if nb_line <= 0:
            print(myFile.read(), end="")
            return
        count_line = 0
        for line in myFile:
            if count_line < nb_line:
                print(line, end="")
            count_line += 1
