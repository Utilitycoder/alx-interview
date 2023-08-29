#!/usr/bin/python3

import sys

"""Solving N Queens problem"""


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at the given position."""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N):
    """Recursive function to solve the N Queens problem."""
    if row == N:
        solution = []
        for i in range(N):
            solution.append([i, board[i].index(1)])
        print(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N)
            board[row][col] = 0


def main():
    """Main entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
