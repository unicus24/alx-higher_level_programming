'''
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>

'''

#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 8 """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle and thus from BaseGeometry, for use with
    rectangular constructs of equal sides.

    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns square area as size * size, invoking Rectangle.area().

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """
        return self.__size ** 2

    def __str__(self):
        """ Provides printable representation of Square object.

        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
