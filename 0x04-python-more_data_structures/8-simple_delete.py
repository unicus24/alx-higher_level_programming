'''
Write a function that deletes a key in a dictionary.

Prototype: def simple_delete(a_dictionary, key=""):
key argument will be always a string
If a key doesn’t exist, the dictionary won’t change
You are not allowed to import any module

'''

#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
