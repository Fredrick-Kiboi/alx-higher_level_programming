#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = sum(a * b for a, b in my_list)
    denominator = sum(b for a, b in my_list)
    return numerator / denominator if denominator != 0 else 0
