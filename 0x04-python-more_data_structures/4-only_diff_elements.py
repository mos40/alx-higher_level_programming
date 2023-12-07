#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Symmetric Difference returns elements active either set, but not in both
    return set_1.symmetric_difference(set_2)
