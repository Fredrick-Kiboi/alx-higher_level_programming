#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ze:
        print(f"Exception: {ze}", file=sys.stderr)
        return None
