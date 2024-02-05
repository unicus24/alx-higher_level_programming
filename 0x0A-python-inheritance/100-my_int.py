'''
Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module

'''




#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 12 """


class MyInt(int):
    """Custom int type inverting behavior of != and == operators.

    """

    def __eq__(self, other):
        """Reverses behavior of == operator.

        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Reverses behavior of != operator.

        """
        return int(self) == int(other)
