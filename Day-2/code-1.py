number = int(input("Enter a number: "))
total = 0
while number > 0:
   total += number % 10 # Extract the last digit
   number //= 10 # Remove the last digit
print("Sum of digits:", total)