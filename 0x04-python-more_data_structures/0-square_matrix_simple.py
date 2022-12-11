#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix.copy()

    for i in range(len(matrix)):
        new_list[i] = list(map(lambda x: x**2, new_list[i]))

        return (new_list)
