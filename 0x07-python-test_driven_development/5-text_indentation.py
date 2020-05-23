#!/usr/bin/python3
"""Function that prints a
    text with 2 new lines
    after ':', '.', '?'
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after ':', '.', '?'
        Args:
            text (str): text to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_ch = [':', '.', '?']
    line_start = True

    for c in text:
        if c == " " and line_start is True:
            continue
        if c in special_ch:
            print(c, end="")
            print('\n')
            line_start = True
        else:
            print(c, end="")
            line_start = False
