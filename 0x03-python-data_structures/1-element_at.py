#!/usr/bin/python3

def element_at(my_list, idx):
    # To check if idx is negative
    if idx < 0:
        return None
    # Check if idx is within the range of the list
    if idx >= len(my_list):
        return None
    # Return the element at the specified index
    return my_list[idx]
