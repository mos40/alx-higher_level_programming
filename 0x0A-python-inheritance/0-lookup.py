#!/usr/bin/python3
"""Defines a function for object attribute lookup."""


def lookup(obj):
    """Returns a list of available attributes for an object."""
    return dir(obj)
