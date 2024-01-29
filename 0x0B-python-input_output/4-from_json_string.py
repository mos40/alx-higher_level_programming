#!/usr/bin/python3
# 6-from_json_string.py
"""Specifies a function for converting a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
