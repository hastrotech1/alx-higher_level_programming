#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({ord(itr_str): None for itr_str in 'cC'})
    return new_str
