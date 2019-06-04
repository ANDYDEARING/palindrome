def is_palindrome(text):
    clean_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    is_pal = True

    for character in text:
        if character.lower() in alphabet:
            clean_text += character.lower()
    n=0
    while is_pal and n<len(clean_text):
        n += 1
        print("working ", n)
    return False
        
user_string = input("Type your text here: ")
is_pal = is_palindrome(user_string)
if is_pal:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")