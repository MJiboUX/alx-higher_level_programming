#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last = int(number[:-1])
if Last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, Last)
elif Last < 5:
    print("Last digit of {:d} is {:d} and is less than 5".format(number, Last)
else:
    print("Last digit of {:d} is {:d} and is zero".format(number, Last)
