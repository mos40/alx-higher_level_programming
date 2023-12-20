#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format the value as an integer
        formatted_value = "{:d}".format(int(value))

        # Print the formatted integer followed by a new line
        print(formatted_value)

        # Return True indicating successful printing
        return True
    except (ValueError, TypeError):
        # Catch exceptions for invalid conversions or types
        return False
