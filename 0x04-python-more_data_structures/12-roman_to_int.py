#!/usr/bin/python3
def roman_to_int(roman_string):
    numberDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = numberDict
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    addit, val = 0, 0
    for n in roman_string:
        if values[n] > val:
            addit += numberDict[n] - val * 2
        else:
            addit += values[n]
        val = values[n]
    return addit
