#!/usr/bin/python3

def print_list_integer(my_list=[]):
  """Prints all integers of a list.

  Args:
    my_list: A list of integers.

  Returns:
    None.
  """

  for integer in my_list:
    print(str.format("{0}", integer))

