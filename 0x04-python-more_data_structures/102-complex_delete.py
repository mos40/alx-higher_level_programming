#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for z, vw in tmp.items():
        if value == vw:
            my_dict.pop(z)
    return my_dict
