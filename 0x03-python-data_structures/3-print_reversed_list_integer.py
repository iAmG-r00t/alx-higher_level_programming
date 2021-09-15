#!/usr/bin/python3
"""A function that prints integers in reverse"""


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
       num = len(my_list) - 1

       while num >= 0:
            print("{:d}".format(my_list[num]))
            num -= 1
