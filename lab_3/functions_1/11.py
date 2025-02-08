def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

word = "madam"
print(is_palindrome(word))
