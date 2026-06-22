# Matrix Multiplication in Python with Validation

def multiply_matrices(A, B):
    """Multiply two matrices A and B if dimensions are compatible."""
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in Matrix A must equal number of rows in Matrix B.")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def read_matrix(rows, cols):
    """Read a matrix from user input with validation."""
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Enter row {i+1} ({cols} numbers): ").split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Invalid input. Please enter exactly {cols} numeric values.")
    return matrix


if __name__ == "__main__":
    try:
        # Read dimensions for Matrix A
        r1 = int(input("Enter number of rows for Matrix A: "))
        c1 = int(input("Enter number of columns for Matrix A: "))

        # Read dimensions for Matrix B
        r2 = int(input("Enter number of rows for Matrix B: "))
        c2 = int(input("Enter number of columns for Matrix B: "))

        # Read matrices
        print("\nEnter Matrix A:")
        A = read_matrix(r1, c1)

        print("\nEnter Matrix B:")
        B = read_matrix(r2, c2)

        # Multiply matrices
        result = multiply_matrices(A, B)

        # Display result
        print("\nResultant Matrix:")
        for row in result:
            print(" ".join(f"{val:.2f}" for val in row))

    except ValueError as e:
        print(f"Error: {e}")
