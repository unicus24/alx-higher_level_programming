#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    thelastdigit = number % -10
else:
    thelastdigit = number % 10
if thelastdigit > 5:
    print("The last digit of {:d} is {:d} and is greater than 5".format(number, thelastdigit))
elif thelastdigit < 6 and thelastdigit != 0:
    print("The last digit of {:d} is {:d} and is less than 6 and not 0".format(number, thelastdigit))
else:
    print("The last digit of {:d} is 0 and is 0".format(number))

