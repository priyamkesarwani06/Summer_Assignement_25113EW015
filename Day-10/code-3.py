def print_number_pyramid(rows):
    """
    Prints a number pyramid pattern like:
        1
       121
      12321
     1234321
    """
    if not isinstance(rows, int) or rows <= 0:
        print("Error: 'rows' must be a positive integer.")
        return

    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Increasing sequence: 1 to i
        for num in range(1, i + 1):
            print(num, end="")

        # Decreasing sequence: i-1 down to 1
        for num in range(i - 1, 0, -1):
            print(num, end="")

        print()  # Move to next line


# Example usage:
try:
    n = int(input("Enter number of rows: "))
    print_number_pyramid(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
