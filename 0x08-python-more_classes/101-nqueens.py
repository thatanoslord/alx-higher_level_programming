#!/usr/bin/python3
import sys

def print_solution(board):
    """Prints the board solution in the required format."""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def is_safe(board, row, col, N):
    """Checks if placing a queen at board[row][col] is safe."""
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N):
    """Solves the N Queens problem using backtracking."""
    if col == N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[i][col] = 0  # Backtrack

    return res

def nqueens(N):
    """Sets up the board and solves the N Queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0, N):
        print("No solution")

if __name__ == "__main__":
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

    nqueens(N)
