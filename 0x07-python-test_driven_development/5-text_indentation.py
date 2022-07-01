#!/usr/bin/python3
"""
Module for text indextation
"""


def text_indentation(text):
    """
    function that prints a text with 2 new
    lines after each of these characters: ., ? and :

    Args:
        text: must be a  string
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ch in text:
        if ch == "." or ch == "?" or ch == ":":
            if ch == ".":
                print(ch, end="")
            if ch == "?" or ch == ":":
                print(ch, end="")
            print("\n")
        else:
            print(ch, end="")
