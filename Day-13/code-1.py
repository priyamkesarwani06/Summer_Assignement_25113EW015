# Program to input and display an array using Python list

def main():
    try:
        # Input number of elements
        n = int(input("Enter number of elements: "))
        if n <= 0:
            print("Array size must be positive.")
            return

        # Input elements
        arr = []
        print(f"Enter {n} elements:")
        for i in range(n):
            value = input(f"Element {i+1}: ")
            arr.append(value)  # Stores as string; convert if needed

        # Display array
        print("\nArray elements are:")
        for i, val in enumerate(arr, start=1):
            print(f"Element {i}: {val}")

    except ValueError:
        print("Invalid input. Please enter integers where required.")

if __name__ == "__main__":
    main()
