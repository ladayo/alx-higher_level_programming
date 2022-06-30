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
    if isinstance(div, float):
        div = int(div)
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    for m_list in matrix:
        if not isinstance(m_list, list):
            raise TypeError("matrix must be a matrix
                            (list of lists) of integers/floats")
    if not all([len(m_list) for m_list in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    n_matrix = [[round((i/div), 2) for i in m_list] for m_list in matrix]
    return n_matrix
