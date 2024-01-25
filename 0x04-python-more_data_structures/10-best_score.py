'''
Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module

'''

#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
