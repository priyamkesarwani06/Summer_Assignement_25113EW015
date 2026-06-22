# Selection Sort Implementation in Python

def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1) - In-place sorting
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        # Find the index of the smallest element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def get_user_input():
    """
    Reads a list of numbers from the user and validates the input.
    """
    try:
        raw_input = input("Enter numbers separated by spaces: ").strip()
        if not raw_input:
            print("No input provided. Exiting.")
            exit(1)
        # Convert input to a list of floats (can handle integers and decimals)
        arr = [float(x) for x in raw_input.split()]
        return arr
    except ValueError:
        print("Invalid input. Please enter only numeric values.")
        exit(1)


if __name__ == "__main__":
    numbers = get_user_input()
    print("Original list:", numbers)
    sorted_list = selection_sort(numbers)
    print("Sorted list (ascending):", sorted_list)
