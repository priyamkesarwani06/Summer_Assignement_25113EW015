# Reverse Star Pattern in Python
# Example: For n = 5
# Output:
# *****
# ****
# ***
# **
# *

def reverse_star_pattern(n):
    # Validate input
    if not isinstance(n, int) or n <= 0:
        print("Please enter a positive integer.")
        return
    
    # Loop to print the pattern
    for i in range(n, 0, -1):
        print("*" * i)

# Main program
try:
    n = int(input("Enter the number of rows: "))
    reverse_star_pattern(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
