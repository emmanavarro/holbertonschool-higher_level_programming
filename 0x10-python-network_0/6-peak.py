#!/usr/bin/python3
""" sends a request to a URL passed as an argument, and displays only the status code of the response """

def find_peak(list_of_integers):
    if len(list_of_integers) is 0:
        return None
    return max(list_of_integers)
