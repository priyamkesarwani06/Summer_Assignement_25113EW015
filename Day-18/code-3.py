# Binary Search Implementation in Python

def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    Returns the index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Middle index
        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found


def main():
    try:
        # Input: sorted list of numbers
        raw_input = input("Enter sorted numbers separated by spaces: ").strip()
        arr = list(map(float, raw_input.split()))
        
        if not arr:
            print("Error: The list cannot be empty.")
            return
        
        # Input: target number
        target = float(input("Enter the number to search: "))
        
        # Perform binary search
        index = binary_search(arr, target)
        
        if index != -1:
            print(f"Element {target} found at index {index}.")
        else:
            print(f"Element {target} not found in the list.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
