#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print up to x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The maximum number of elements from my_list to print.

    Returns:
        The actual number of elements printed.
    """
    elements_displayed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_displayed += 1
        except IndexError:
            break
    print("")
    return elements_displayed
