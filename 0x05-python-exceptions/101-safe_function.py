#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        fct(*args)
        return result
    except ZeroDivisionError as ze:
        print("Exception: {}".format(ze), file=sys.stderr)
        return None
    except IndexError as ie:
        print("Exception: {}".format(ie), file=sys.stderr)
        return None
