# Program to find all pairs in a list whose sum equals a given target

def find_pairs_with_sum(numbers, target_sum):
    """
    Finds all unique pairs in 'numbers' that sum up to 'target_sum'.
    Returns a list of tuples.
    """
    seen = set()       # Stores numbers we've seen so far
    pairs = set()      # Stores unique pairs

    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            # Store pairs in sorted order to avoid duplicates like (3,7) and (7,3)
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return list(pairs)


def main():
    try:
        # Input list of integers
        raw_input = input("Enter numbers separated by spaces: ").strip()
        if not raw_input:
            print("Error: No numbers entered.")
            return

        numbers = list(map(int, raw_input.split()))

        # Input target sum
        target_sum_input = input("Enter target sum: ").strip()
        if not target_sum_input.lstrip('-').isdigit():
            print("Error: Target sum must be an integer.")
            return
        target_sum = int(target_sum_input)

        # Find pairs
        result_pairs = find_pairs_with_sum(numbers, target_sum)

        # Output results
        if result_pairs:
            print(f"Pairs with sum {target_sum}:")
            for pair in result_pairs:
                print(pair)
        else:
            print(f"No pairs found with sum {target_sum}.")

    except ValueError:
        print("Error: Please enter valid integers only.")


if __name__ == "__main__":
    main()
