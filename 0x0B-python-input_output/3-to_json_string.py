#!/usr/bin/python3

"""To JSON string"""
import json


def to_json_string(my_obj):
    """
        JSON representation of an object (string)

        Args:
            my_obj: object to convert to JSON

        Return: JSON Representation
    """
    return(json.dumps(my_obj))
