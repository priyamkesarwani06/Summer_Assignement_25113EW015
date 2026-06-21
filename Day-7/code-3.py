def sum_of_digits(n):
    """
    Recursively calculates the sum of digits of an integer.
    Handles negative numbers by converting them to positive.
    """
    n = abs(n)  # Ensure the number is positive
    if n < 10:  # Base case: single-digit number
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)  # Recursive step


def main():
    try:
        # Take user input
        num = int(input("Enter an integer: "))
        
        result = sum_of_digits(num)
        print(f"Sum of digits of {num} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
