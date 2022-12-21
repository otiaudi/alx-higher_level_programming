#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    my_list=[]: List of elements to print
    x: The number of elements in a list.

    Return: returns the number of elements.
    """

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")

        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1
    print()
    return (count)
