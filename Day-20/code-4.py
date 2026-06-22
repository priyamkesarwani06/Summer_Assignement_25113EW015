# Program to find column-wise sum of a nested list (matrix)

def column_wise_sum(matrix):
    """
    Returns a list containing the sum of each column in the matrix.
    Handles empty matrices and validates uniform row lengths.
    """
    if not matrix or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Matrix must be a non-empty list of lists.")

    # Ensure all rows have the same length
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise ValueError("All rows must have the same number of columns.")

    # Calculate column-wise sum
    col_sums = [0] * row_length
    for row in matrix:
        for col_index, value in enumerate(row):
            if not isinstance(value, (int, float)):
                raise ValueError("Matrix elements must be numbers.")
            col_sums[col_index] += value

    return col_sums


# Example usage
if __name__ == "__main__":
    try:
        # Example matrix
        matrix = [
            [3, 7, 6],
            [1, 3, 5],
            [9, 3, 2]
        ]

        result = column_wise_sum(matrix)
        print("Column-wise sum:", result)

    except ValueError as e:
        print("Error:", e)
