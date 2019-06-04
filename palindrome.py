def is_palindrome(text):
    return False
user_string = input("Type your text here: ")
is_pal = is_palindrome(user_string)
if is_pal:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")