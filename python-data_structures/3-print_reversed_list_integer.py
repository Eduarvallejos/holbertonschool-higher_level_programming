#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    last_num = None
    for num in reversed(my_list):
        print("{}".format(num))
        last_num = num
        return last_num
