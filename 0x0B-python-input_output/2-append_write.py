#!/usr/bin/python3

"""Append to a file"""


def append_write(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        and returns the number of characters written

         Args:
            filename: name of file to be read and printed
            text: string to be written to file

        Return:
            number of charaters written
    """

    with open(filename, mode='a', encoding="utf-8") as f:
        append_chars = f.write(text)
        return append_chars
