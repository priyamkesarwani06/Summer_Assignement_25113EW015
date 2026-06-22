# Program to transpose a matrix in Python

def transpose_matrix(matrix):
    """
    Returns the transpose of a given matrix.
    Transpose means converting rows into columns and vice versa.
    """
    if not matrix or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Matrix must be a list of lists.")
    
    # Ensure all rows have the same length
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise ValueError("All rows in the matrix must have the same length.")
    
    # Transpose using zip and unpacking
    return [list(row) for row in zip(*matrix)]


def main():
    try:
        # Input matrix dimensions
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows <= 0 or cols <= 0:
            print("Rows and columns must be positive integers.")
            return
        
        # Input matrix elements
        matrix = []
        print("Enter the matrix row by row (space-separated values):")
        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                print(f"Error: Row must have exactly {cols} elements.")
                return
            matrix.append(row)
        
        # Transpose and display
        transposed = transpose_matrix(matrix)
        print("\nOriginal Matrix:")
        for row in matrix:
            print(row)
        
        print("\nTransposed Matrix:")
        for row in transposed:
            print(row)
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
