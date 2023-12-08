#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Test whether the key exists in the dictionary
    if key in a_dictionary:
        # Deletes the key-value pair if it existed
        del a_dictionary[key]

    # Bring back the modified dictionary
    return a_dictionary
