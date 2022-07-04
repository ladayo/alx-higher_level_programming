#!/usr/bin/python3

"""Lookup"""


def lookup(obj):
    """
    returns the list of availble attributes and methods of a class

    Args:
        obj: object
    Return:
        list of object and attributes
    """
    return dir(obj)
