# Program to merge two arrays in Python

def merge_arrays(arr1, arr2):
    """
    Merges two arrays (lists) into one.
    Returns a new list containing elements of both arrays.
    """
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Both inputs must be lists.")
    return arr1 + arr2  # Concatenate lists


def main():
    try:
        # Input first array
        n1 = int(input("Enter number of elements in first array: "))
        if n1 < 0:
            print("Size cannot be negative.")
            return
        arr1 = []
        for i in range(n1):
            value = input(f"Enter element {i+1} for first array: ")
            arr1.append(value)

        # Input second array
        n2 = int(input("Enter number of elements in second array: "))
        if n2 < 0:
            print("Size cannot be negative.")
            return
        arr2 = []
        for i in range(n2):
            value = input(f"Enter element {i+1} for second array: ")
            arr2.append(value)

        # Merge arrays
        merged = merge_arrays(arr1, arr2)

        # Display result
        print("\nFirst Array:", arr1)
        print("Second Array:", arr2)
        print("Merged Array:", merged)

    except ValueError:
        print("Invalid input. Please enter integers for sizes.")
    except TypeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
