#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Use a list comprehension to create a new dict with unwanted keys removed
    updated_dict = {key: val for key, val in a_dict.items() if val != value}

    # Update the original dictionary with the modified one
    a_dictionary.clear()
    a_dictionary.update(updated_dict)
