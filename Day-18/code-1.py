# Bubble Sort Implementation in Python

def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization: track if any swap happened
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return arr


def get_input_list():
    """
    Reads a list of numbers from user input with validation.
    """
    try:
        raw_input = input("Enter numbers separated by spaces: ").strip()
        if not raw_input:
            print("Empty input. Please enter at least one number.")
            return None
        # Convert input to a list of floats (supports integers and decimals)
        return [float(x) for x in raw_input.split()]
    except ValueError:
        print("Invalid input. Please enter only numeric values.")
        return None


if __name__ == "__main__":
    numbers = get_input_list()
    if numbers is not None:
        sorted_numbers = bubble_sort(numbers)
        print("Sorted list:", sorted_numbers)
