# Program to remove duplicates from an array in Python

def remove_duplicates(arr):
    """Remove duplicates from the list while preserving order."""
    seen = set()
    unique_list = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

def main():
    try:
        # Take input from the user
        raw_input_data = input("Enter array elements separated by spaces: ").strip()
        
        if not raw_input_data:
            print("The array is empty. Nothing to remove.")
            return
        
        # Convert input to a list of integers
        arr = list(map(int, raw_input_data.split()))
        
        # Remove duplicates
        result = remove_duplicates(arr)
        
        print("Array after removing duplicates:", result)
    
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
