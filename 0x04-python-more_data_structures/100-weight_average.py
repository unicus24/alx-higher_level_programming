'''
Write a function that returns the weighted average of all integers tuple (<score>, <weight>)

Prototype: def weight_average(my_list=[]):
Returns 0 if the list is empty
You are not allowed to import any module

'''

#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    quotient = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        quotient += tup[1]
    return float(average / quotient)
