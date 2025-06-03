#!/usr/bin/python3
"""Defines a function that converts class attributes to a serializable dict."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization."""
    return obj.__dict__
