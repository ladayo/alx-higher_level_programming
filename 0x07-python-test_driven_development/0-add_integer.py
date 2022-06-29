#!/usr/bin/python3
"""
module to add two integers
"""
def add_integer(a, b=98):
    """
    function to add two integers

    Args:
        a is an integer
        b is an integer
    """
    if (isinstance(a, int) == False) and (isinstance(a, float) == False):
        raise TypeError("a must be an integer")
    if (isinstance(b, int) == False) and (isinstance(b, float) == False):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
