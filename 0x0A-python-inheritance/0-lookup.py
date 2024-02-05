'''
Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module

'''






#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 0 """


def lookup(obj):
    
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (any): object of any type

    Returns:
        list of available attributes and methods

    """
    return dir(obj)
