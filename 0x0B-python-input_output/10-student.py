#!/usr/bin/python3
"""
Defines "Student" class
"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student's information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
         with filter"""
        res = {}
        if attrs is not None:
            for a in attrs:
                try:
                    res[a] = self.__dict__[a]
                except:
                    pass
            return res
        return self.__dict__
