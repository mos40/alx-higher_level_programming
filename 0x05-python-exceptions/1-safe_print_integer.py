#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The value that may represent an integer

    Returns:
        If a TypeError or ValueError occurs - False otherwise
        Otherwise - True if the value is successfully printed as integer
    """
    try:
        formatted_interger = "{:d}".format(int(value))
        print(formatted_integer)
        # print("{:d}".format(value)) #
        return (True)
    except (TypeError, ValueError):
        return (False)
