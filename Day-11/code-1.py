# Function to find the sum of two numbers
def sum_of_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    Parameters:
        a (int/float): First number
        b (int/float): Second number
    Returns:
        int/float: Sum of a and b
    """
    # Ensure inputs are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be integers or floats.")
    return a + b


# Main program
if __name__ == "__main__":
    try:
        # Take user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Call the function
        result = sum_of_two_numbers(num1, num2)

        # Display the result
        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except TypeError as te:
        print(f"Error: {te}")
