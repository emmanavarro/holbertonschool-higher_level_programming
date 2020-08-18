#!/usr/bin/python3
""" sends a request to a URL passed as an argument, and displays only the status code of the response """

def find_peak(list_of_integers):
    """Find peak in list"""
    listt = list_of_integers.copy()
    for idx in range(len(listt)):
        if (idx - 1) >= 0 and (idx + 1) <= (len(listt) - 1):
            if listt[idx] >= listt[idx - 1] and listt[idx] >= listt[idx + 1]:
                return listt[idx]
        if (idx - 1) < 0:
            if listt[idx] >= listt[idx + 1]:
                return listt[idx]
        if (idx + 1) > (len(listt) - 1):
            if listt[idx] >= listt[idx - 1]:
                return listt[idx]
    return None
