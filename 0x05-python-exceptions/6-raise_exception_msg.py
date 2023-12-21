#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a name exception with a specified message.

    Args:
        message (str): The message for the exception.

    Raises:
        NameError: Always raises a NameError with the provided message.
    """
    raise NameError(message)
