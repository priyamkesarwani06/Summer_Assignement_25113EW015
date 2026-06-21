# Program to print a centered alphabet palindrome pyramid

def print_char_pyramid(rows):
    if not isinstance(rows, int) or rows <= 0:
        print("Error: Number of rows must be a positive integer.")
        return

    for i in range(1, rows + 1):
        # Print leading spaces for centering
        print(" " * (rows - i), end="")

        # Increasing sequence: A, AB, ABC, ...
        for j in range(i):
            print(chr(ord('A') + j), end="")

        # Decreasing sequence: BA, CBA, DCBA, ...
        for j in range(i - 2, -1, -1):
            print(chr(ord('A') + j), end="")

        print()  # Move to next line


# Example usage
try:
    n = int(input("Enter number of rows: "))
    print_char_pyramid(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
