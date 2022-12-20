#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ To print x elements of a list.
    args:
    my_list: The list to be printed from.
    x(int): The number of elements in my_list.

    Return:
    The number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print(" ")
    return (count)
