# Read input from user
n = int(input("Enter a natural number: "))
if n < 1:
   print("Please enter a positive integer.")
else:
   total = 0
   for i in range(1, n + 1):
       total += i
   print(f"The sum of the first {n} natural numbers is: {total}") 