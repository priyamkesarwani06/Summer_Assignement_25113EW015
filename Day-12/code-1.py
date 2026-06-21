import string

def is_palindrome(text):
    """
    Check if the given text is a palindrome.
    Ignores case, spaces, and punctuation.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # Remove spaces and punctuation, convert to lowercase
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())

    # Compare cleaned string with its reverse
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    try:
        user_input = input("Enter a string to check if it's a palindrome: ")
        if is_palindrome(user_input):
            print("✅ It's a palindrome!")
        else:
            print("❌ It's not a palindrome.")
    except ValueError as e:
        print(f"Error: {e}")
