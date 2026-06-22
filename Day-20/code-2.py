# Program to check if a matrix is symmetric

def is_symmetric(matrix):
    """
    Checks if the given matrix is symmetric.
    A symmetric matrix must be square and equal to its transpose.
    """
    # Validate matrix is not empty
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Check if matrix is square
    if rows != cols:
        return False

    # Compare elements with their transpose positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def main():
    try:
        # Input matrix size
        n = int(input("Enter the size of the square matrix (n): "))
        if n <= 0:
            print("Matrix size must be positive.")
            return

        matrix = []
        print(f"Enter the {n}x{n} matrix row by row (space-separated integers):")
        for _ in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                print("Invalid row length. Please enter exactly", n, "elements.")
                return
            matrix.append(row)

        # Check symmetry
        if is_symmetric(matrix):
            print("The matrix is symmetric.")
        else:
            print("The matrix is NOT symmetric.")

    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
