def power(x, n):
    """
    Compute x^n without using pow() or ** operator.
    Uses binary exponentiation for O(log n) time complexity.
    Handles negative exponents and zero cases.
    """
    # Input validation
    if not isinstance(x, (int, float)) or not isinstance(n, int):
        raise ValueError("Base must be int/float and exponent must be int.")

    # Special case: 0^0 is undefined
    if x == 0 and n == 0:
        raise ValueError("0^0 is undefined.")

    # Special case: 0 raised to positive exponent is 0
    if x == 0:
        return 0

    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        # If n is odd, multiply result by current x
        if n % 2 == 1:
            result *= x
        # Square the base
        x *= x
        # Divide exponent by 2
        n //= 2

    return result


# Example usage
try:
    base = float(input("Enter base (x): "))
    exponent = int(input("Enter exponent (n): "))
    print(f"{base}^{exponent} = {power(base, exponent)}")
except ValueError as e:
    print("Error:", e)
