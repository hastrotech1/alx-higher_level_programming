#!/usr/bin/python3
def max_integer(my_list=None):

    if my_list is None:
        return 'None'

    elif len(my_list) == 0:
        return 'None'

    else:
        max_val = my_list[0]

        for u in range(1, len(my_list)):

            if my_list[u] > max_val:
                max_val = my_list[u]

        return max_val
