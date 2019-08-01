"""Define a function is_palindrome() that recognizes palindromes"""


def is_palindrome(string1):
    if string1[::-1] == string1:
        return "This is palindrome"
    else:
        return "This is not palindrome"


string = input("Enter string for checking palindrome : ")

print(is_palindrome(string))
