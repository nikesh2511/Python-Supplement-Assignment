# Problem 8: Check if a string is palindrome
# Find and fix the
def is_palindrome(text):
    text = text.lower()  # make it case-insensitive
    return text == text[::-1]

word = "Racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
