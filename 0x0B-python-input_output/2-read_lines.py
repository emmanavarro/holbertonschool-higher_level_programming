#!/usr/bin/python3
"""In this module it create a function that read
    n lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a
    text file and prints it to stdout
    """

    with open(filename, encoding='utf-8') as my_file:

        count_line = 0

        for line in my_file:
            count_line += 1
            if (nb_lines <= 0) or (nb_lines == count_line):
                print(line, end='')

    my_file.close()
