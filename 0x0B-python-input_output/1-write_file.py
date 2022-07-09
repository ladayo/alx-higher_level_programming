#!/usr/bin/python3

"""Write to a file"""


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        and returns the number of characters written

         Args:
            filename: name of file to be read and printed
            text: string to be written to file

        Return:
            number of charaters written
    """

    with open(filename, mode='w', encoding="utf-8") as f:
        written_chars = f.write(text)
        return written_chars
