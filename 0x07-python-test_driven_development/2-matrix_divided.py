#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix
    Matrix must be a list of lists
    of integers, floats.
    Return: a new matrix
    """

    if not isinstance(matrix, list) or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) is not len(element):
            raise TypeError("Each row of the matrix must have the same size")
        for j in element:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    return[[round(j / div, 2) for j in i] for i in matrix]
