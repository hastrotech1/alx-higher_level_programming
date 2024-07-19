#!/usr/bin/python3

def uniq_add(my_list=[]):

    unik_list = set(my_list)

    n = 0

    for num in unik_list:

        n += num

    return (n)