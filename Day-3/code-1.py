def generate_fibonacci(n):
    # Initializing the first two terms
    a, b = 0, 1
    
    # Generate and print the sequence
    for _ in range(n):
        print(a, end=" ")
        # Updating variables simultaneously
        a, b = b, a + b

# Example usage: Generate the first 10 terms
num_terms = 10
print(f"Fibonacci series with {num_terms} terms:")
generate_fibonacci(num_terms)
