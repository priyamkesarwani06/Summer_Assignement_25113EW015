# Binary to Decimal Conversion in Python

def binary_to_decimal(binary_str):
    """
    Convert a binary string to its decimal equivalent.
    :param binary_str: str, binary number as a string
    :return: int, decimal equivalent
    """
    try:
        # Validate that the string contains only 0s and 1s
        if not all(ch in '01' for ch in binary_str):
            raise ValueError("Input must contain only 0 and 1.")

        # Convert using int() with base 2
        decimal_value = int(binary_str, 2)
        return decimal_value

    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Take user input
    binary_input = input("Enter a binary number: ").strip()

    # Convert and display result
    decimal_result = binary_to_decimal(binary_input)
    if decimal_result is not None:
        print(f"Decimal equivalent of {binary_input} is: {decimal_result}")
