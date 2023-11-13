"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def ValidPalindrome(s: str) -> bool:
    if len(s) == 0:
        return True
    string = s
    test_string = "".join(
        letter for letter in string.replace(" ", "").lower() if letter.isalnum()
    )
    if test_string == test_string[::-1]:
        return True
    else:
        return False


print(ValidPalindrome(" "))
