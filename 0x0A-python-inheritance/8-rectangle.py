'''
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

'''

#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 8 """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry, for use with rectangular constructs.

    Args:
        width (int): x dimension of rectangle
        height (int): y dimension of rectangle

    Attributes:
        __width (int): x dimension of rectangle
        __height (int): y dimension of rectangle

    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
