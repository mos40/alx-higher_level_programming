#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dict is empty
    if not a_dictionary:
        return None

    # Get the key with the maximum val
    best_key = max(a_dictionary, key=a_dictionary.get)

    # Bring back the key with the highest integer val
    return best_key
