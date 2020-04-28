#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = ord(letter) - 32
        else:
            letter = ord(letter)
        print("{:c}".format(letter), end='')
    print("")
