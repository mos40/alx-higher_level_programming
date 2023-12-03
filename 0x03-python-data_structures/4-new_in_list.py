#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Test if the idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Bring back copy of original list

    # Create new list with element replaced at the specified index
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
