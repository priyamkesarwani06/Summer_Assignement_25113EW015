# Program to print a number triangle: 
# 1
# 12
# 123
# 1234
# 12345

def print_number_triangle(rows):
    # Validate input
    if not isinstance(rows, int) or rows <= 0:
        print("Error: 'rows' must be a positive integer.")
        return
    
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")  # Print numbers on the same line
        print()  # Move to the next line

# Main execution
try:
    n = int(input("Enter the number of rows: "))
    print_number_triangle(n)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
