def is_palindrome(string):
    return string == string[::-1]

pol = input()
if is_palindrome(pol):
    print(pol, "is palindrome")
else:
    print(pol, "is not palindrome")