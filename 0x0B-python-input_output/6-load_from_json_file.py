#!/usr/bin/python3
"""Specifies a function for reading a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from the content of a JSON file."""
    with open(filename) as file:
        return json.load(file)
