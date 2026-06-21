# Factorial function with input validation
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Returns the factorial value.
    Raises ValueError for negative inputs.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Main program
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is: {factorial(num)}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"Unexpected error: {e}")
