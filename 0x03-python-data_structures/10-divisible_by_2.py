#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the elements of the input list
    for num in my_list:
        # Checks if the number is a multiple of 2
        is_multiple_of_2 = (num % 2 == 0)

        # Appends the result to the new list
        result_list.append(is_multiple_of_2)

    return result_list
