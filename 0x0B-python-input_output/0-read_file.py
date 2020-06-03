#!/usr/bin/python3
'''Read text file module'''


def read_file(filename=""):
    '''Read function'''

    with open('my_file_0.txt', mode='r', encoding='utf-8') as my_file:
        print(my_file.read(), end='')
