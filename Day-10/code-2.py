# Reverse Pyramid Pattern in Python

def reverse_pyramid(rows):
    """
    Prints a reverse pyramid pattern of stars.
    :param rows: Number of rows in the pyramid
    """
    if not isinstance(rows, int) or rows <= 0:
        print("Error: rows must be a positive integer.")
        return

    for i in range(rows, 0, -1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Example usage
try:
    n = int(input("Enter number of rows: "))
    reverse_pyramid(n)
except ValueError:
    print("Invalid input. Please enter an integer.")

