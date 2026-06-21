# Star Pyramid Program in Python

def print_star_pyramid(rows):
    """
    Prints a center-aligned star pyramid.
    :param rows: Number of rows in the pyramid (positive integer)
    """
    if not isinstance(rows, int) or rows <= 0:
        print("Error: Number of rows must be a positive integer.")
        return

    for i in range(1, rows + 1):
        # Print spaces for alignment
        spaces = ' ' * (rows - i)
        # Print stars (odd numbers: 1, 3, 5, ...)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


# Main program
try:
    n = int(input("Enter the number of rows for the pyramid: "))
    print_star_pyramid(n)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
