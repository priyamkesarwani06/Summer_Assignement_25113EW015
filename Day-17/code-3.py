# Intersection of two arrays in Python
# Handles duplicates based on frequency in both arrays

def intersection(arr1, arr2):
    """
    Returns the intersection of two lists, including duplicates.
    """
    result = []
    arr2_copy = arr2.copy()  # Copy to avoid modifying the original list

    for item in arr1:
        if item in arr2_copy:
            result.append(item)
            arr2_copy.remove(item)  # Remove to handle duplicates correctly
    return result


def get_list_input(prompt):
    """
    Reads a list of integers from user input with validation.
    """
    while True:
        try:
            return list(map(int, input(prompt).strip().split()))
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")


if __name__ == "__main__":
    print("Enter elements for the first array (space-separated integers):")
    array1 = get_list_input("Array 1: ")

    print("Enter elements for the second array (space-separated integers):")
    array2 = get_list_input("Array 2: ")

    result = intersection(array1, array2)

    print(f"Intersection of the arrays: {result}")
