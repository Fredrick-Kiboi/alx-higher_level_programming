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
    """Prints an integer with `{:d}`.format().

  Args:
    value: The integer to print.

  Returns:
    True if the integer was printed successfully, False otherwise.

  Raises:
    ValueError: If the value is not an integer.
    """

    if isinstance(value, int):
        print("{:d}".format(value))
        return True
    elif value is None:
        print("The value is None.")
        return False
    elif isinstance(value, list):
        if 89 in value:
            print("The value contains the number 89.")
            return True
        else:
            print("The value does not contain the number 89.")
            return False
    else:
        print("The value is not an integer.")
        return False


if __name__ == "__main__":
    value = {89}
    print(safe_print_integer(value))

    value = None
    print(safe_print_integer(value))

    value = [89]
    print(safe_print_integer(value))
