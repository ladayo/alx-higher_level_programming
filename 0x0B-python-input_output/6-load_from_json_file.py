#!/usr/bin/python3

"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
        decodes or deserializes a string representation
        and creates an object respectively
        Args:
            filename: name of file
    """

    with open(filename, encoding="utf-8") as f:
        decode = json.load(f)  # deserializes the JSON from textfile to object
    return (decode)
