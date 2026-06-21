def move_zeroes_to_end(arr):
    """
    Moves all zeroes in the list 'arr' to the end while maintaining
    the relative order of non-zero elements.
    This function modifies the list in place.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    # Pointer for the position of the next non-zero element
    pos = 0

    # First pass: move non-zero elements forward
    for num in arr:
        if not isinstance(num, (int, float)):
            raise ValueError("List must contain only numbers.")
        if num != 0:
            arr[pos] = num
            pos += 1

    # Second pass: fill the rest with zeroes
    while pos < len(arr):
        arr[pos] = 0
        pos += 1


# Example usage
if __name__ == "__main__":
    try:
        nums = [0, 1, 0, 3, 12, 0, 5]
        print("Original list:", nums)
        move_zeroes_to_end(nums)
        print("After moving zeroes:", nums)
    except (TypeError, ValueError) as e:
        print("Error:", e)
