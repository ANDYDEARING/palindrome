def is_palindrome(text, is_clean=False):
    is_pal = True
    if not is_clean:
        clean_text = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for character in text:
            if character.lower() in alphabet:
                clean_text += character.lower()
        text = clean_text
    return is_pal
        
user_string = input("Type your text here: ")
is_pal = is_palindrome(user_string)
if is_pal:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")