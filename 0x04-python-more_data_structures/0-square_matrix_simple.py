#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix.copy()
    for i in new_list:
        return [x**2 for x in i]
