'''
Write a function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module
'''

#!/usr/bin/python3
def uniq_add(my_list=[]):
    return(sum(set(my_list)))
