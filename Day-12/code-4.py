def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    A perfect number is equal to the sum of its proper divisors.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    # Find divisors and sum them
    divisor_sum = 1  # 1 is always a divisor (for n > 1)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid adding square root twice
                divisor_sum += n // i

    return divisor_sum == n and n != 1


# Example usage
try:
    num = int(input("Enter a positive integer: "))
    if is_perfect_number(num):
        print(f"{num} is a Perfect Number.")
    else:
        print(f"{num} is NOT a Perfect Number.")
except ValueError as e:
    print("Error:", e)
