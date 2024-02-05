'''
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module

'''

#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 7 """


class BaseGeometry:
    """Intentionally empty area() method.

    """
    def area(self):
        """Unimplemented, only raises exception to notify user.

        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Input filtration for integers: checks if value is an int above 0.
        No use of self, could be staticmethod.

        Args:
            name (str): name bound to object
            value (any): value of object, expecting int

        Exceptions:
            TypeError: if `value` is not an int
            ValueError: if `value` is less than or equal to 0

        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

