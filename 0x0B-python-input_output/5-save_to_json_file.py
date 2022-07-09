#!/usr/bin/python3

"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
        Object to a text file,
        using a JSON representation

        Args:
            filename: name of file to write into
            my_obj: object to convert to JSON
    """

    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)  # serializes(writes) the object to a text file
