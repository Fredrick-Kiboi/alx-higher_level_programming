#!/usr/bin/python3

"""Prints x elemnts of a list

Prototype:
    def safe_print_list(my_list=[], x=0):

    Args:
    my_list (list): the list containing the elements
    x (int): number of elements to be printed

Returns:
    int: The actual number of elements printed
"""


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    Args:
        my_list (list): The list containing the elements.
        x (int): The number of elements to be printed.

    Returns:
        int: The actual number of elements printed.
    """
    try:
        count = 0
        for i in range(x):
            print(f"{my_list[i]}", end="")
            count += 1
    except Exception:
        pass
    finally:
        print()
        return (count)
