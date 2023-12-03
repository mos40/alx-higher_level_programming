#!/usr/bin/env python3

def no_c(my_string):
    # Initialize an empty str to store the res
    result = ""

    # Repeatedly execute through each char in the input str
    for char in my_string:
        # Test if the char is not 'c' or 'C'
        if char.lower() != 'c':
            result += char

    return result
