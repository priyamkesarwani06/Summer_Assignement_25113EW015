# Half Pyramid Pattern in Python

def print_half_pyramid(rows):
    """Prints a half pyramid pattern with the given number of rows."""
    for i in range(1, rows + 1):
        print("*" * i)  # Print i stars in each row


def main():
    try:
        # Take user input
        rows = int(input("Enter the number of rows for the half pyramid: "))

        # Validate input
        if rows <= 0:
            print("Please enter a positive integer greater than zero.")
            return

        # Print the pattern
        print("\nHalf Pyramid Pattern:")
        print_half_pyramid(rows)

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
