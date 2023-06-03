#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        fct(*args)
        return result
    except Exception as ze:
        print("Exception: {}".format(ze), file=sys.stderr)
        return None
