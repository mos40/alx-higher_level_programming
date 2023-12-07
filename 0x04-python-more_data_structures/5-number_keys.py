#!/usr/bin/python3
def number_keys(a_dictionary):
    # Tests if the input is a dictionary
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input is not a dictionary")

    # Count and return the num of keys
    return len(a_dictionary.keys())
