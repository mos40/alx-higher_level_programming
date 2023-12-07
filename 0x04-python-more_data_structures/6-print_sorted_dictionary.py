#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Test if the input is a dictionary
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input is not a dictionary")

    # Arrange the keys alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Show the dictionary with ordered keys
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
