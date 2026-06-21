import math

def is_strong_number(num):
    """
    Check if a number is a Strong Number.
    A Strong Number is a number whose sum of factorial of digits equals the number itself.
    """
    if num < 0:
        return False  # Negative numbers cannot be strong numbers

    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)  # Factorial of each digit
        temp //= 10

    return total == num


def main():
    try:
        # Take user input
        num = int(input("Enter a number: "))

        # Check and display result
        if is_strong_number(num):
            print(f"{num} is a Strong Number ✅")
        else:
            print(f"{num} is NOT a Strong Number ❌")

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
