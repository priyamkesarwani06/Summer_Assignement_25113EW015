def is_palindrome_numeric(num):
    if num < 0: return False
    original, reversed_num = num, 0
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10
    return original == reversed_num
