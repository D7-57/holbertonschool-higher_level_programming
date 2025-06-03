#!/usr/bin/python3
"""Defines a Student class that can be a JSON."""


class Student:
    """Class represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, list=[0]):
        """Return a dictionary representation of the Student

         with specified items to return
         """
        OriginalDict = self.__dict__
        if list == [0]:
            """if empty return all"""
            return OriginalDict
        else:
            """not empty return the items wanted"""
            dict = {}
            for i in list:
                if i in OriginalDict:
                    dict[i] = OriginalDict[i]
            return dict

    def reload_from_json(self, json):
        """change the current student data with the given JSON"""
        if json == {}:
            return
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
