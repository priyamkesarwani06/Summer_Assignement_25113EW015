# Program to sort an array in descending order

def sort_descending(arr):
    """
    Sorts the given list in descending order.
    """
    # Using built-in sort() with reverse=True
    arr.sort(reverse=True)
    return arr

def main():
    try:
        # Taking input from the user
        raw_input = input("Enter numbers separated by spaces: ").strip()
        
        if not raw_input:
            print("Error: No input provided.")
            return
        
        # Convert input string to list of numbers
        arr = list(map(float, raw_input.split()))
        
        # Sort in descending order
        sorted_arr = sort_descending(arr)
        
        print("Sorted array in descending order:", sorted_arr)
    
    except ValueError:
        print("Error: Please enter valid numbers only.")

if __name__ == "__main__":
    main()
