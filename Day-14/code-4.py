from collections import Counter
arr = [1, 2, 3, 2, 5, 1]
# Count occurrences of each element
counter = Counter(arr)
# Extract elements with count > 1
duplicates = [item for item, count in counter.items() if count > 1]
print("Duplicates:", duplicates)
# Output: Duplicates: [1, 2]