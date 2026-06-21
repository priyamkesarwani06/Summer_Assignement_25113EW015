def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.
    Handles both positive and negative integers.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # For negative numbers, use two's complement representation for 32 bits
    if n < 0:
        n = n & 0xFFFFFFFF  # Mask to 32 bits

    count = 0
    while n:
        count += n & 1  # Increment if last bit is 1
        n >>= 1         # Shift right by 1
    return count


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        result = count_set_bits(num)
        print(f"Number of set bits in {num} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
