#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Return a set containing common elements between two sets.

    Parameters:
    - set_1 (set): The first set.
    - set_2 (set): The second set.

    Returns:
    - set: A set containing common elements.
    """
    return set_1.intersection(set_2)
