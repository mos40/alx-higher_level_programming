#!/usr/bin/python3
"""Defines a function to add attributes to objects."""


def add_attribute(obj, attribute_name, attribute_value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        attribute_name (str): The name of the attribute to add to obj.
        attribute_value (any): The value of the new attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute")
    
    setattr(obj, attribute_name, attribute_value)
