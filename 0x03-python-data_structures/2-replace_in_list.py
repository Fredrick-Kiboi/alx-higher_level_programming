#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        new_list = my_list
        return new_list
    elif idx >= len(my_list):
        new_list = my_list
        return my_list
    else:
        new_list = my_list
        new_list[idx] = element
        return new_list
