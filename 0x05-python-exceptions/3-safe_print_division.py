#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b.
    Returns:
        int or None: The result of the division,
        or None if an error occurs."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
