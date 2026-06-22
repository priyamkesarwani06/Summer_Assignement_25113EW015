# Program to find the sum of diagonals in a square matrix

def diagonal_sum(matrix):
    """
    Calculate the sum of primary and secondary diagonals of a square matrix.
    Avoids double-counting the center element for odd-sized matrices.
    """
    n = len(matrix)
    total_sum = 0
    
    for i in range(n):
        total_sum += matrix[i][i]               # Primary diagonal
        total_sum += matrix[i][n - i - 1]       # Secondary diagonal
    
    # If matrix size is odd, subtract the center element (counted twice)
    if n % 2 == 1:
        total_sum -= matrix[n // 2][n // 2]
    
    return total_sum


def main():
    try:
        # Input matrix size
        n = int(input("Enter the size of the square matrix (n): "))
        if n <= 0:
            print("Matrix size must be a positive integer.")
            return
        
        matrix = []
        print(f"Enter the {n}x{n} matrix row by row (space-separated integers):")
        
        for i in range(n):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != n:
                print("Each row must have exactly", n, "elements.")
                return
            matrix.append(row)
        
        # Calculate and display the diagonal sum
        result = diagonal_sum(matrix)
        print("Sum of both diagonals:", result)
    
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
if __name__ == "__main__":
    main()
