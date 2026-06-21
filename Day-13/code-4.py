# Program to count even and odd elements in a list

def count_even_odd(numbers):
    """Counts even and odd numbers in a list."""
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if isinstance(num, int):  # Ensure the element is an integer
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            print(f"Warning: Skipping non-integer value '{num}'")
    
    return even_count, odd_count


if __name__ == "__main__":
    try:
        # Take input from the user
        raw_input_data = input("Enter numbers separated by spaces: ").strip()
        
        if not raw_input_data:
            print("No input provided.")
        else:
            # Convert input to a list of integers
            numbers_list = []
            for item in raw_input_data.split():
                try:
                    numbers_list.append(int(item))
                except ValueError:
                    print(f"Warning: '{item}' is not a valid integer and will be skipped.")
            
            # Count even and odd numbers
            even, odd = count_even_odd(numbers_list)
            
            # Display results
            print(f"Even numbers count: {even}")
            print(f"Odd numbers count: {odd}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
