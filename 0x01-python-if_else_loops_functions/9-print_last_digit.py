#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastDigit = abs(number) % 10
    else:
        lastDigit = number % 10
    print("{0:d}".format(lastDigit), end="")
    return lastDigit
