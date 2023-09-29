#!/usr/bin/python3
"""
    Rotate a 2D matrix in place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix in place.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None: The function modifies the input matrix in place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        # After rotation:
        # matrix = [[7, 4, 1],
        #           [8, 5, 2],
        #           [9, 6, 3]]
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
