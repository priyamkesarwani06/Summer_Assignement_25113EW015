def factorial(n):
    """
    Recursive function to calculate factorial of a non-negative integer.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    try:
        # Take user input
        num = int(input("Enter a non-negative integer: "))

        # Validate input
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return

        # Calculate factorial
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
