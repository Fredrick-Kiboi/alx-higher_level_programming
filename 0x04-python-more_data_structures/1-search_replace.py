#!/usr/bin/python3


"""
Function that replaces all occurences of an element
by another in a new list

Args:
    my_list: initial list
    search: element to replace in the list
    replace: new element

Returns:
    new_list
"""


def search_replace(my_list, search, replace):
  new_list = my_list[:]
  for i in range(len(new_list)):
      if new_list[i] == search:
          new_list[i] = replace
  return (new_list)
