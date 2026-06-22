from collections import Counter

def max_frequency_elements(lst):
    """
    Returns the element(s) with the highest frequency in the list.
    Handles empty lists and ties.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:
        return None, 0  # No elements in the list

    # Count frequency of each element
    freq_counter = Counter(lst)

    # Find the maximum frequency
    max_freq = max(freq_counter.values())

    # Get all elements with the maximum frequency
    max_elements = [elem for elem, freq in freq_counter.items() if freq == max_freq]

    return max_elements, max_freq


# Example usage
if __name__ == "__main__":
    try:
        # Example list
        data = [1, 2, 2, 3, 1, 4, 2, 3, 3, 3]

        elements, frequency = max_frequency_elements(data)

        if elements is None:
            print("The list is empty.")
        else:
            print(f"Element(s) with maximum frequency: {elements}")
            print(f"Frequency: {frequency}")

    except Exception as e:
        print(f"Error: {e}")
