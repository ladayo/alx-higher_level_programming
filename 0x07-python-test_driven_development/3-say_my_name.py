#!/usr/bin/python3
"""
Module to say my name
"""


def say_my_name(first_name, last_name=""):
    """
    function to print  my first and last name

    Args:
        first_name: user first name
        last_name: user last name
    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if first_name.isdigit():
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name.isdigit():
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
