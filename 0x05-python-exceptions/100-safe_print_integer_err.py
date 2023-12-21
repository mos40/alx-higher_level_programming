#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer and returns True if successful, False otherwise.

    If a ValueError is caught, a corresponding error message
    is printed to standard error.

    Args:
        value: Any value that may represent an integer.

    Returns:
        bool: True if the value is successfully
        printed as an integer, False otherwise.
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
