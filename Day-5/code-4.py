def largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of a given integer n.
    If n <= 1, returns None.
    """
    if n <= 1:
        return None  # No prime factors for numbers <= 1

    # Handle negative numbers by taking absolute value
    n = abs(n)

    largest_factor = None

    # Remove factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Check odd factors from 3 upwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2  # Skip even numbers

    # If n is still > 2, it is prime
    if n > 2:
        largest_factor = n

    return largest_factor


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        result = largest_prime_factor(num)

        if result is None:
            print(f"{num} has no prime factors.")
        else:
            print(f"The largest prime factor of {num} is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
