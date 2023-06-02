#!/usr/bin/python3
"""
safe_print_integer(value)

Prints an integer with "{:d}".format().

Args:
  value: The integer to print.

Returns:
  True if the integer was printed successfully, False otherwise.

Raises:
  ValueError: If the value is not an integer.
"""

def safe_print_integer(value):
  try:
    print("{:d}".format(value))
    return True
  except ValueError:
    return False