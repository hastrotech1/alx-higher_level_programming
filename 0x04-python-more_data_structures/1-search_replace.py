#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = list(map(lambda _list: replace if _list == search else _list, my_list))

    return (new_list)
