import math

def is_prime(n):
    """
    Check if a number is prime.
    Returns True if prime, False otherwise.
    """
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime

    # Eliminate even numbers and multiples of 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):  # Check numbers of form 6k ± 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
