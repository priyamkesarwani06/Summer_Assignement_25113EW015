# Rotate an array to the right by k positions

def rotate_right(arr, k):
    """
    Rotates the array to the right by k positions.
    Handles negative k and k > len(arr).
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, (int, float, str)) for x in arr):
        raise ValueError("Array elements must be numbers or strings.")
    if not isinstance(k, int):
        raise TypeError("Rotation count must be an integer.")
    if len(arr) == 0:
        return arr  # Empty array remains unchanged

    k = k % len(arr)  # Normalize k to avoid extra rotations
    return arr[-k:] + arr[:-k] if k != 0 else arr


if __name__ == "__main__":
    try:
        # Take array input from user
        raw_input = input("Enter array elements separated by spaces: ").strip()
        arr = raw_input.split()  # Treats input as strings; can be converted if needed

        # Take rotation count
        k = int(input("Enter number of positions to rotate right: "))

        rotated = rotate_right(arr, k)
        print("Rotated Array:", rotated)

    except ValueError as ve:
        print("Value Error:", ve)
    except TypeError as te:
        print("Type Error:", te)
    except Exception as e:
        print("Unexpected Error:", e)
