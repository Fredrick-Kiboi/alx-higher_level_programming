#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tupleadd = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            tupleadd[i] += tuple_a[i]
        if i < len(tuple_b):
            tupleadd[i] += tuple_b[i]
    return tuple(tupleadd)
