# Program to print a character triangle pattern
# Pattern:
# A
# AB
# ABC
# ABCD
# ABCDE

def print_character_triangle(rows):
    # Validate input
    if not isinstance(rows, int) or rows <= 0:
        print("Error: Number of rows must be a positive integer.")
        return
    
    for i in range(1, rows + 1):
        # chr(65) is 'A', so chr(65 + j) gives next letters
        for j in range(i):
            print(chr(65 + j), end="")
        print()  # Move to the next line

# Example usage
try:
    n = int(input("Enter number of rows (max 26): "))
    if n > 26:
        print("Warning: Only first 26 uppercase letters are available. Limiting to 26.")
        n = 26
    print_character_triangle(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
