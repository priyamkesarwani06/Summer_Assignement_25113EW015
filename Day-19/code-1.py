# Program to add two matrices in Python

def read_matrix(rows, cols):
    """Reads a matrix of given dimensions from user input."""
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Enter row {i+1} ({cols} numbers): ").split()))
                if len(row) != cols:
                    raise ValueError(f"Row must have exactly {cols} numbers.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    return matrix


def add_matrices(matrix1, matrix2):
    """Adds two matrices element-wise."""
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result


def print_matrix(matrix):
    """Prints a matrix in a readable format."""
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))


if __name__ == "__main__":
    try:
        # Read matrix dimensions
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")

        print("\nEnter first matrix:")
        matrix1 = read_matrix(rows, cols)

        print("\nEnter second matrix:")
        matrix2 = read_matrix(rows, cols)

        # Add matrices
        result = add_matrices(matrix1, matrix2)

        # Display result
        print("\nResultant Matrix after Addition:")
        print_matrix(result)

    except ValueError as e:
        print(f"Error: {e}")
