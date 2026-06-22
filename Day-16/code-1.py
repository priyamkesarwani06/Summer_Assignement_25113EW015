# Program to find the missing number in an array from 1 to n

def find_missing_number(arr):
    """
    Finds the missing number in an array containing numbers from 1 to n with one missing.
    :param arr: List[int] - input array
    :return: int - the missing number
    """
    if not arr:
        raise ValueError("Array cannot be empty.")

    n = len(arr) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing = expected_sum - actual_sum

    if missing <= 0 or missing > n:
        raise ValueError("Invalid array: no valid missing number found.")

    return missing


if __name__ == "__main__":
    try:
        # Example: user input
        raw_input = input("Enter numbers separated by spaces (from 1 to n with one missing): ").strip()
        arr = list(map(int, raw_input.split()))

        # Validate input: all numbers should be positive integers
        if any(num <= 0 for num in arr):
            raise ValueError("All numbers must be positive integers.")

        missing_number = find_missing_number(arr)
        print(f"The missing number is: {missing_number}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
