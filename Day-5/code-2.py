import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Check divisors up to sqrt(num)
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def print_primes_in_range(start, end):
    """Print all prime numbers in the given range."""
    if start > end:
        start, end = end, start  # Swap if range is reversed
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    if primes:
        print(f"Prime numbers between {start} and {end}:")
        print(*primes)
    else:
        print(f"No prime numbers found between {start} and {end}.")

if __name__ == "__main__":
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        print_primes_in_range(start, end)
    except ValueError:
        print("Invalid input. Please enter integer values only.")
