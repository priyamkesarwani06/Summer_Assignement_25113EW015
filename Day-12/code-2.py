def is_armstrong(number):
    """
    Check if a number is an Armstrong number.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if Armstrong, False otherwise.
    """
    # Validate input type
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Convert number to string to easily iterate digits
    digits = str(number)
    num_digits = len(digits)

    # Calculate sum of each digit raised to the power of num_digits
    total = sum(int(digit) ** num_digits for digit in digits)

    return total == number


# Main program
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        if is_armstrong(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is NOT an Armstrong number.")
    except ValueError as e:
        print(f"Error: {e}")
