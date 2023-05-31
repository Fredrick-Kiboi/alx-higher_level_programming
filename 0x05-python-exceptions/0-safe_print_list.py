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

    The function attempts to print the specified number of elements from the given list. If the length of the list
    is less than x, it will print as many elements as possible and return the actual count. It uses a try-except block
    for error handling to ensure that the program continues execution even if an exception occurs.
    
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
    except:
        pass
    finally:
        print()
        return (count)