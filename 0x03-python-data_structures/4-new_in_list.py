#!/usr/bin/python3

"""
replaces an element in a list
"""

def new_in_list(my_list, idx, element):

    copy_new_list = my_list.copy()

    copied_list_len = len(my_list)

    if idx < 0 or idx >= copied_list_len:
        return (copy)
    else:
        copy_new_list[idx] = element

    return (copy_new_list)
