#!/usr/bin/python3
def matrix_divided(matrix, div):
    error_message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_message)

    for sublist in matrix:
        if not isinstance(sublist, list):
            raise TypeError(error_message)
        for item in sublist:
            if not isinstance(item, (int, float)):
                raise TypeError(error_message)

    for sublist in matrix:
        if len(sublist) == 0:
            raise TypeError(error_message)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not all(len(sublist) == len(matrix[0]) for sublist in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in sublist] for sublist in matrix]
