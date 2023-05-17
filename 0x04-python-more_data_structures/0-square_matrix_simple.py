#!/usr/bin/python3

"""
function that computes the squre value of the integers of a matrix

Args:
    2D array;  A Matrix

Returns:
    New matrix
    Same size as the original matrix
    Each value should be the square of the input
"""

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])
