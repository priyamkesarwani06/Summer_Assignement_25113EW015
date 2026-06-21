# Program to find the largest and smallest element in Python

def find_largest_smallest(numbers):
    """Return the largest and smallest numbers from the list."""
    if not numbers:
        raise ValueError("The list is empty. Cannot find largest and smallest values.")
    return max(numbers), min(numbers)


def main():
    try:
        # Take input from the user
        raw_input = input("Enter numbers separated by spaces: ").strip()
        
        if not raw_input:
            print("No input provided.")
            return
        
        # Convert input to a list of floats (supports integers and decimals)
        numbers = []
        for item in raw_input.split():
            try:
                numbers.append(float(item))
            except ValueError:
                print(f"Invalid number skipped: {item}")
        
        if not numbers:
            print("No valid numbers entered.")
            return
        
        # Find largest and smallest
        largest, smallest = find_largest_smallest(numbers)
        
        print(f"Largest number: {largest}")
        print(f"Smallest number: {smallest}")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
