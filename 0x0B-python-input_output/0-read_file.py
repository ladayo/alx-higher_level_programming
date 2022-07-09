#!/usr/bin/python3

""" Read file"""


def read_file(filename=""):
    """
         reads a text file (UTF8) and prints it to stdou

         Args:
            filename: name of file to be read and printed
    """

    with open(filename, mode='r', encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
