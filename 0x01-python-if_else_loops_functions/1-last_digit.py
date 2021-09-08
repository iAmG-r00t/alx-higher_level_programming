#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of " + str(number) + " is "

if number < 0:
    digit = number % (-10)
else:
    digit = number % 10

if digit > 5:
    print("{} {} and is greater than 5".format(string, digit))
elif digit == 0:
    print("{} {} and is 0".format(string, digit))
else:
    print("{} {} and is less than 6 and not 0".format(string, digit))
