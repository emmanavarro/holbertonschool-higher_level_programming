#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for index in range(0, len(matrix)):
        newMatrix.append(list(map((lambda x: x * x), matrix[index])))
    return newMatrix
