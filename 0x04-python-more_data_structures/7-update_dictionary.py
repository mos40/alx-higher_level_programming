#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Verifys if the input is a dictionary
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input is not a dictionary")

    # Update / add the key-value pair
    a_dictionary[key] = value
