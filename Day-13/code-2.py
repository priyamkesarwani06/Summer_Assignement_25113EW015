# Program to find sum and average of an array in Python

def get_numbers():
    """Reads a list of numbers from user input with validation."""
    try:
        # Read input as space-separated values
        arr = list(map(float, input("Enter numbers separated by spaces: ").strip().split()))
        if not arr:  # Empty list check
            raise ValueError("Array cannot be empty.")
        return arr
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def calculate_sum_and_average(arr):
    """Calculates sum and average of a list of numbers."""
    total_sum = sum(arr)
    average = total_sum / len(arr)
    return total_sum, average

def main():
    arr = get_numbers()
    if arr is None:
        return  # Exit if invalid input
    
    total_sum, average = calculate_sum_and_average(arr)
    
    print(f"Sum of array elements: {total_sum}")
    print(f"Average of array elements: {average}")

if __name__ == "__main__":
    main()
