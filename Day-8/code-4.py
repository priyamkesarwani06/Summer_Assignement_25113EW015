# Program to print repeated-number pattern in Python

def print_pattern(n):
    """
    Prints a pattern where each line contains the line number repeated that many times.
    Example for n=5:
    1
    22
    333
    4444
    55555
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        print("Please enter a positive integer.")
        return

    for i in range(1, n + 1):
        print(str(i) * i)  # Repeat the number i, i times


# Main execution
try:
    # Take user input
    num = int(input("Enter the number of lines for the pattern: "))
    print_pattern(num)
except ValueError:
    print("Invalid input. Please enter an integer.")
