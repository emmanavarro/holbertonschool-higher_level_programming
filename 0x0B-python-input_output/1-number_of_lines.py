#!/usr/bin/python3
'''Number of lines module'''


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""

    with open('my_file_0.txt', mode='r', encoding='utf-8') as my_file:

        count_line = 0

        for line in my_file:
            count_line += 1
        return count_line
