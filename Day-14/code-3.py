# Program to find the second largest element in a list

def second_largest(numbers):
    """
    Returns the second largest unique number in the list.
    Raises ValueError if there are fewer than two unique numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    # Remove duplicates and sort in descending order
    unique_numbers = sorted(set(numbers), reverse=True)

    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two unique elements.")

    return unique_numbers[1]  # Second largest


if __name__ == "__main__":
    try:
        # Example input
        data = [10, 20, 4, 45, 99, 99, 20]
        print("List:", data)
        result = second_largest(data)
        print("Second largest element is:", result)

    except (TypeError, ValueError) as e:
        print("Error:", e)
