#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for element in row:
            # Displace each element with formatting
            print("{:d}".format(element), end=" ")
        print()
