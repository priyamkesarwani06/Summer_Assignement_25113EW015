# Program to find row-wise sum of a matrix

def row_wise_sum(matrix):
    """
    Returns a list containing the sum of each row in the matrix.
    """
    return [sum(row) for row in matrix]

def main():
    try:
        # Input matrix dimensions
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            print("Rows and columns must be positive integers.")
            return

        matrix = []
        print(f"Enter the matrix elements row by row ({cols} numbers per row):")
        for i in range(rows):
            while True:
                try:
                    row = list(map(float, input(f"Row {i+1}: ").split()))
                    if len(row) != cols:
                        print(f"Please enter exactly {cols} numbers.")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values only.")

        # Calculate row-wise sums
        sums = row_wise_sum(matrix)

        # Display results
        print("\nRow-wise sums:")
        for i, total in enumerate(sums, start=1):
            print(f"Sum of row {i}: {total}")

    except ValueError:
        print("Invalid input. Please enter integers for dimensions.")

if __name__ == "__main__":
    main()
