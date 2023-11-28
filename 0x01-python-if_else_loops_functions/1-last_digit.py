#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Define strings for different scenarios
greater_than_5 = " and is greater than 5"
is_zero = " and is 0"
less_than_6_not_zero = " and is less than 6 and not 0"

# Determine the last digit of the number
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Check and print the scenario based on the last digit
if last_digit > 5:
    print("Last digit of {} is {}{}".format(number, last_digit, greater_than_5))
elif last_digit == 0:
    print("Last digit of {} is {}{}".format(number, last_digit, is_zero))
else:
    print("Last digit of {} is {}{}".format(number, last_digit, less_than_6_not_zero))

