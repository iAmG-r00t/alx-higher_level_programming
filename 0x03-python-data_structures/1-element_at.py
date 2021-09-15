#!/usr/bin/python3
"""A function that retrieves an element from a list like in C"""


def element_at(my_list, idx):
    if idx < 0:
        return (None)

    length = len(my_list)

    if idx > length - 1:
        return (None)

    return(my_list[idx])
