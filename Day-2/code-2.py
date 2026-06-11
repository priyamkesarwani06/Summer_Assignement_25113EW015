def reverse_number_string(number):
   if number < 0:
       return -int(str(-number)[::-1])
   return int(str(number)[::-1])
# Example
print(reverse_number_string(12345))
print(reverse_number_string(-9876)) 