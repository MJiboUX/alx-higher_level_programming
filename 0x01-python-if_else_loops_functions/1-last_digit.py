#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[:-1] > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, number [:-1]))
elif number[:-1] < 5:
    print("Last digit of {:d} is {:d} and is less than 5".format(number, number [:-1]))
else:
    print("Last digit of {:d} is {:d} and is zero".format(number, number [:-1]))
