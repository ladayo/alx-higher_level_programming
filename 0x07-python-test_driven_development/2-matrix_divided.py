#!/usr/bin/python3
"""
Module to divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function to divide elements in a list a number

    Args:
        matrix: list of lists
        div: an integer or float
    Returns:
        new matrix containg the result
    """
    prev_len = 0
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if isinstance(div, float):
        div = int(div)
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(error)
    for m_list in matrix:
        if not isinstance(m_list, list):
            raise TypeError(error)
        for item in m_list:
            if type(item) is not int and type(item) is not float:
                raise TypeError(error)
        if len(m_list) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(m_list)
    n_matrix = [[round((i/div), 2) for i in m_list] for m_list in matrix]
    return n_matrix
