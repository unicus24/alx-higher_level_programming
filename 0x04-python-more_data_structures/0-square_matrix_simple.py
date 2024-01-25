#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    NewMatrix = [row[:] for row in matrix]
    for idx, row in enumerate(NewMatrix):
        for idx2, col in enumerate(NewMatrix):
            NewMatrix[idx][idx2] = row[idx2] ** 2
    return NewMatrix 
