#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Do a new matrix with the same size as the input matrix
    resMatrix = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]

    # Iterate through each element of the matrix & calculate the square
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            resMatrix[i][j] = matrix[i][j] ** 2

    return resMatrix
