# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols, name):
    """
    Read a matrix from the user, row by row.

    Parameters:
    rows (int): Number of rows.
    cols (int): Number of columns.
    name (str): Label used in the input prompt (e.g., "A" or "B").

    Returns:
    list: A 2D list representing the matrix.
    """
    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        row = [int(val) for val in row_values]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """
    Display a matrix in a neat, aligned grid format.

    Parameters:
    matrix (list): A 2D list to display.
    """
    for row in matrix:
        print(" ".join(f"{val:4}" for val in row))


def transpose_matrix(matrix):
    """
    Compute the transpose of a matrix using nested loops.

    Parameters:
    matrix (list): The original M x N matrix.

    Returns:
    list: The transposed N x M matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """
    Add two matrices of the same size element-wise.

    Parameters:
    matrix_a (list): First matrix.
    matrix_b (list): Second matrix.

    Returns:
    list: The resulting matrix after addition.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply matrix A (M x N) by matrix B (N x P) using nested loops.

    Parameters:
    matrix_a (list): M x N matrix.
    matrix_b (list): N x P matrix.

    Returns:
    list: The resulting M x P matrix.
    """
    m = len(matrix_a)
    n = len(matrix_b)
    p = len(matrix_b[0])
    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


if __name__ == "__main__":
    print("--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols, "Matrix")

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    print("\n--- PART B: Add Two Matrices ---")
    add_rows = int(input("Enter number of rows: "))
    add_cols = int(input("Enter number of columns: "))
    print("Matrix A:")
    matrix_a = read_matrix(add_rows, add_cols, "A")
    print("Matrix B:")
    matrix_b = read_matrix(add_rows, add_cols, "B")

    print("\nSum of Matrices:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A / rows of Matrix B: "))
    p = int(input("Enter columns of Matrix B: "))
    print("Matrix A:")
    mult_a = read_matrix(m, n, "A")
    print("Matrix B:")
    mult_b = read_matrix(n, p, "B")

    print("\nProduct of Matrices:")
    print_matrix(multiply_matrices(mult_a, mult_b))
