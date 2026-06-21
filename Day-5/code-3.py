# Program to print all factors of a given number

def find_factors(n):
    """Return a sorted list of factors of n."""
    factors = set()
    for i in range(1, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(abs(n) // i)
    return sorted(factors)

def main():
    try:
        # Take user input
        num = int(input("Enter an integer: "))
        
        # Handle zero separately
        if num == 0:
            print("Every non-zero integer is a factor of 0.")
            return
        
        # Get and print factors
        factors = find_factors(num)
        print(f"Factors of {num} are: {factors}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
