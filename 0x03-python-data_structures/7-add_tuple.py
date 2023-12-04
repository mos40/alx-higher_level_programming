#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the 1st & 2nd elements from each tuple, using 0 if not present
    a1, a2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b1, b2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    # Calculate the sum of corresponding elements
    sum_1 = a1 + b1
    sum_2 = a2 + b2

    # Return the result as a tuple
    return (sum_1, sum_2)
