# Program to find the GCD of two numbers in Python

def gcd(a, b):
    """Compute the Greatest Common Divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Ensure GCD is always positive

def main():
    try:
        # Take input from the user
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        
        # Calculate GCD
        result = gcd(num1, num2)
        
        print(f"The GCD of {num1} and {num2} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
