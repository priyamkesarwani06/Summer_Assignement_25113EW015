# Program to find common elements between two lists

def get_list_input(prompt):
    """Reads a list of integers from user input with validation."""
    while True:
        try:
            # Split input by spaces and convert to integers
            return list(map(int, input(prompt).strip().split()))
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

def find_common_elements(list1, list2):
    """Finds and returns sorted list of common elements."""
    # Convert to sets for fast intersection
    common = set(list1) & set(list2)
    return sorted(common)  # Sorted for consistent output

if __name__ == "__main__":
    # Read two lists from the user
    list1 = get_list_input("Enter elements of first list (space-separated): ")
    list2 = get_list_input("Enter elements of second list (space-separated): ")

    # Find common elements
    common_elements = find_common_elements(list1, list2)

    # Display results
    if common_elements:
        print("Common elements:", common_elements)
    else:
        print("No common elements found.")
