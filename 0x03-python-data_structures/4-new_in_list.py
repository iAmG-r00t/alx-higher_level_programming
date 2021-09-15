#!/usr/bin/python3
"""a function that replaces an element in a list at a specific position without modifying the original list"""


def new_in_list(my_list, idx, element):
    length = len(my_list)

    copy_list = my_list[:]

    if 0 <= idx < length:
        copy_list[idx] = element

    return(copy_list)
