#!/usr/bin/python3
import random

# Generate a random number between -10 and 10
number = random.randint(-10, 10)

# Check and print the nature of the number
if number < 0:
    print("The number {} is negative.".format(number))
elif number == 0:
    print("The number {} is zero.".format(number))
else:
    print("The number {} is positive.".format(number))
