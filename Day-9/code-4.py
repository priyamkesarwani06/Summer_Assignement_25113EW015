# Hollow Square Star Pattern in Python

def print_hollow_square(size):
    # Validate input
    if not isinstance(size, int) or size < 1:
        print("Error: Size must be a positive integer.")
        return
    
    for row in range(size):
        for col in range(size):
            # Print star for first/last row or first/last column
            if row == 0 or row == size - 1 or col == 0 or col == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to next line

# Example usage
try:
    n = int(input("Enter the size of the square: "))
    print_hollow_square(n)
except ValueError:
    print("Invalid input. Please enter an integer.")

