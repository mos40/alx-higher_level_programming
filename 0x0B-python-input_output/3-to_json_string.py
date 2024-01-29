#!/usr/bin/python3
"""Defines a function for converting a string to its JSON representation."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of the given object."""
    return json.dumps(my_obj)
