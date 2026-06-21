import math

def find_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers.
    Handles negative numbers and zero.
    """
    if a == 0 or b == 0:
        return 0  # LCM involving zero is zero
    return abs(a * b) // math.gcd(a, b)

def main():
    try:
        # Take user input
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        
        # Calculate LCM
        lcm_value = find_lcm(num1, num2)
        
        # Display result
        print(f"LCM of {num1} and {num2} is: {lcm_value}")
    
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
