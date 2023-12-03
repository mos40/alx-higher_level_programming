#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
