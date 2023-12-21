#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct (function): The function to be executed.
        *args: Arguments to be passed to the function.

    Returns:
        The result of the function if successful, None otherwise.
    """
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
