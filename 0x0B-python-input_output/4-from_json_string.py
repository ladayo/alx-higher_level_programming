#!/usr/bin/python3

""" From JSON string to Object"""
import json


def from_json_string(my_str):
    """
        object (Python data structure) represented by a JSON string

        Args:
            my_str: JSON to convert to object

        Return: Object Representation
    """
    return(json.loads(my_str))
