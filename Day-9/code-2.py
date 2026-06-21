# Reverse Number Triangle Pattern
# Example for n = 5:
# 12345
# 1234
# 123
# 12
# 1

def reverse_number_triangle(n):
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    for i in range(n, 0, -1):  # Start from n down to 1
        for j in range(1, i + 1):  # Print numbers from 1 to i
            print(j, end="")
        print()  # Move to the next line


# Example usage:
try:
    n = int(input("Enter the number of rows: "))
    reverse_number_triangle(n)
except ValueError as e:
    print("Error:", e)
