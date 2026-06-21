from collections import Counter

def frequency_counter(lst):
    """
    Returns a dictionary with the frequency of each element in the list.
    Uses collections.Counter for efficiency.
    """
    return dict(Counter(lst))

def frequency_manual(lst):
    """
    Returns a dictionary with the frequency of each element in the list.
    Uses manual dictionary counting.
    """
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

def main():
    try:
        # Input: space-separated elements
        user_input = input("Enter elements separated by spaces: ").strip()
        
        if not user_input:
            print("Error: No input provided.")
            return
        
        # Convert input into a list (strings by default)
        elements = user_input.split()
        
        # Method 1: Using Counter
        print("\nFrequency using Counter:")
        print(frequency_counter(elements))
        
        # Method 2: Manual counting
        print("\nFrequency using manual dictionary method:")
        print(frequency_manual(elements))
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
