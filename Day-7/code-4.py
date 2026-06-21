def reverse_number(num, rev=0):
    """
    Recursively reverse the digits of an integer.
    Handles both positive and negative numbers.
    """
    # Base case: when number becomes 0, return the reversed number
    if num == 0:
        return rev
    else:
        return reverse_number(num // 10, rev * 10 + num % 10)


def main():
    try:
        # Take input from user
        user_input = input("Enter an integer to reverse: ").strip()

        # Validate integer input
        num = int(user_input)

        # Handle negative numbers separately
        if num < 0:
            reversed_num = -reverse_number(-num)
        else:
            reversed_num = reverse_number(num)

        print(f"Reversed number: {reversed_num}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()

