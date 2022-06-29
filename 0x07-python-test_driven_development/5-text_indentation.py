#!/usr/bin/python3
"""
Module for text indextation
"""
def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: must be a  string
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indent_chars = ('.', '?', ':')
    start_idx = 0

    for idx, current_char in enumerate(text):
        if current_char in indent_chars:
            print(text[start_idx:idx + 1].strip() + '\n')
            start_idx = idx + 1
    print(text[start_idx:].strip(), end="")
