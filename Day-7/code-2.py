# Recursive function to calculate Fibonacci number
def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    n must be a non-negative integer.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    try:
        # Take user input
        terms = int(input("Enter the number of terms for Fibonacci sequence: "))
        
        if terms <= 0:
            print("Please enter a positive integer greater than 0.")
            return
        
        print(f"Fibonacci sequence up to {terms} terms:")
        for i in range(terms):
            print(fibonacci(i), end=" ")
        print()  # Newline after sequence

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


if __name__ == "__main__":
    main()
