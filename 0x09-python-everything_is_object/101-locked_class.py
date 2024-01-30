#!/usr/bin/python3
'''
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

You are not allowed to import any module

'''


class LockedClass:
    """if user defined, no new items can be added to list"""
    __slots__ = ['first_name']
