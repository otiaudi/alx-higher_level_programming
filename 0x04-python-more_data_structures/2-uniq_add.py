#!/usr/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    num = 0
    for i in new_list:
        num += i
    return (num)
