# Get input from the user
num = int(input("Enter a number: "))

# Initialize sum variable
digit_sum = 0

# Loop until the number becomes 0
while num > 0:
    remainder = num % 10    
    digit_sum += remainder   
    num = num // 10         

# Display the final output
print("The sum of the digits is:", digit_sum)
