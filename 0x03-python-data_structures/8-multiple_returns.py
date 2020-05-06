#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        tupl = (len(sentence), None)
        return tupl
    else:
        tupl = (len(sentence), sentence[0])
        return tupl
