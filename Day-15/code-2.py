# Rotate an array to the left by d positions
def rotate_left(arr, d):
    # Handle empty array
    if not arr:
        return []

    n = len(arr)
    # Normalize d to be within array length
    d = d % n

    # If d is negative, convert it to equivalent left rotation
    if d < 0:
        d = n + d

    # Perform rotation using slicing
    return arr[d:] + arr[:d]


if __name__ == "__main__":
    try:
        # Input array
        arr_input = input("Enter array elements separated by spaces: ").strip()
        if not arr_input:
            print("Array cannot be empty.")
            exit(1)

        arr = list(map(int, arr_input.split()))

        # Input rotation count
        d = int(input("Enter number of positions to rotate left: "))

        rotated = rotate_left(arr, d)
        print("Rotated array:", rotated)

    except ValueError:
        print("Invalid input. Please enter integers only.")
