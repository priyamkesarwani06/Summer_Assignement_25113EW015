# Fibonacci sequence generator in Python

def fibonacci(n):
    """
    Generate a list containing the first n Fibonacci numbers.
    :param n: Number of terms (must be a non-negative integer)
    :return: List of Fibonacci numbers
    """
    if not isinstance(n, int):
        raise TypeError("Number of terms must be an integer.")
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Main program
if __name__ == "__main__":
    try:
        terms = int(input("Enter the number of Fibonacci terms: "))
        result = fibonacci(terms)
        print(f"Fibonacci sequence ({terms} terms): {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
