#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = matrix.copy()

    for sq_matrix in range(len(matrix)):

        new_matrix[sq_matrix] = list(map(lambda x: x**2, matrix[sq_matrix]))

    return(new_matrix)
