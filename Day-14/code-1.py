# Linear Search in Python with input validation

def linear_search(arr, target):
    """
    Perform linear search on the given list.
    Returns the index of the target if found, else -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index  # Found at this index
    return -1  # Not found


def main():
    try:
        # Input list of numbers
        raw_input = input("Enter numbers separated by spaces: ").strip()
        if not raw_input:
            print("Error: No input provided.")
            return
        
        arr = list(map(int, raw_input.split()))
        
        # Input target number
        target_input = input("Enter the number to search: ").strip()
        if not target_input:
            print("Error: No target provided.")
            return
        
        target = int(target_input)
        
        # Perform search
        result = linear_search(arr, target)
        
        # Output result
        if result != -1:
            print(f"Element {target} found at index {result}.")
        else:
            print(f"Element {target} not found in the list.")
    
    except ValueError:
        print("Error: Please enter valid integers only.")


if __name__ == "__main__":
    main()
