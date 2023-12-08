#!/usr/bin/python3
ef multiply_by_2(a_dictionary):
    # Create a new dictionary to store the modified values
    result_dictionary = {}

    # Iterate through the items in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply each value by 2 and add it to the new dictionary
        result_dictionary[key] = value * 2

    # Return the new dictionary with modified values
    return result_dictionary
