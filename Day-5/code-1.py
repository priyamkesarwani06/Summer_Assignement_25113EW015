# Perfect Number Checker in Python

def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a perfect number.
    A perfect number is equal to the sum of its proper divisors.
    """
    if n <= 1:
        return False  # Perfect numbers are positive integers > 1

    divisors_sum = 1  # 1 is always a divisor
    # Loop till sqrt(n) to find divisors efficiently
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid adding square root twice
                divisors_sum += n // i

    return divisors_sum == n


def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        if is_perfect_number(num):
            print(f"{num} is a Perfect Number ✅")
        else:
            print(f"{num} is NOT a Perfect Number ❌")

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
