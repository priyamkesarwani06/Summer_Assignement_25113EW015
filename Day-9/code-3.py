# Program to print repeated character pattern: A, BB, CCC, DDDD, EEEEE

def print_repeated_char_pattern(n):
    """
    Prints a pattern where each row contains the same letter repeated
    row_number times, starting from 'A'.
    
    Example for n=5:
    A
    BB
    CCC
    DDDD
    EEEEE
    """
    if not isinstance(n, int) or n <= 0:
        print("Error: Please enter a positive integer.")
        return

    for i in range(n):
        # chr(65) is 'A', so chr(65 + i) gives the next letter
        char = chr(65 + i)
        print(char * (i + 1))

# Example usage:
try:
    rows = int(input("Enter number of rows (max 26): "))
    if rows > 26:
        print("Warning: Only first 26 uppercase letters are available. Limiting to 26.")
        rows = 26
    print_repeated_char_pattern(rows)
except ValueError:
    print("Invalid input. Please enter an integer.")
