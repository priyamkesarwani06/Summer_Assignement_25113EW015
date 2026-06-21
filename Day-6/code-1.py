# Decimal to Binary Conversion in Python

def decimal_to_binary(n: int) -> str:
    """
    Convert a decimal integer to its binary representation.
    Handles negative numbers as well.
    """
    if n == 0:
        return "0"
    elif n < 0:
        return "-" + decimal_to_binary(-n)  # Handle negative numbers
    
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))  # Get remainder (0 or 1)
        n //= 2  # Integer division by 2
    
    binary_digits.reverse()  # Reverse to get correct order
    return "".join(binary_digits)


if __name__ == "__main__":
    try:
        # Take user input
        decimal_number = int(input("Enter a decimal integer: "))
        
        # Convert and display
        binary_representation = decimal_to_binary(decimal_number)
        print(f"Binary representation: {binary_representation}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

