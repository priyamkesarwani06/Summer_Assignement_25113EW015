def find_max(numbers):
    """
    Function to find the maximum value in a list of numbers.
    :param numbers: list of integers or floats
    :return: maximum value
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) == 0:
        raise ValueError("List is empty. Cannot find maximum.")

    # Ensure all elements are numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid element '{num}'. All elements must be numbers.")

    # Initialize max_value with the first element
    max_value = numbers[0]

    # Iterate through the list to find the maximum
    for num in numbers[1:]:
        if num > max_value:
            max_value = num

    return max_value


# Example usage
if __name__ == "__main__":
    try:
        # Example list
        data = [12, 45, 7, 89, 23, 89.5, -10]
        result = find_max(data)
        print(f"The maximum value in the list is: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
