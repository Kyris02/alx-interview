#!/usr/bin/python3

""" This module rotates a 2D matrix clockwise."""


def rotate_2d_matrix(matrix):
    """ This function takes the matrix as an argument
    and rotates it clowise."""

    lengthOfArray = len(matrix)

    # Transpose the matrix (push box from left to right)
    for i in range(lengthOfArray):
        for j in range(i + 1, lengthOfArray):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row (last row first, first row last)
    for i in range(lengthOfArray):
        matrix[i] = matrix[i][::-1]


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
