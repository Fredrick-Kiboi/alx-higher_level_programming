#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    summation = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            summation[i] += tuple_a[i]
        if i < len(tuple_b):
            summation[i] += tuple_b[i]
        return tuple(summation)
