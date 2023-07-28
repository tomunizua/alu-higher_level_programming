#!/usr/bin/python3
"""Python class of student"""


class Student():
    """A class of student"""

    def __init__(self, first_name, last_name, age):
        """Inintializing attributes.

        args:
            self.first_name = first_nam of student
            self.last_name = last_name of student
            self.age = age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dict representation of student class"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
