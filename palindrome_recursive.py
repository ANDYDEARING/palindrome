def is_palindrome(text, is_clean=False):
    """Finds whether or not text is a palindrome with recursive logic"""
    if not is_clean:
        clean_text = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for character in text:
            if character.lower() in alphabet:
                clean_text += character.lower()
        text = clean_text
    if len(text) <= 1:
        return True
    elif len(text) == 2:
        return (text[0] == text[-1])
    elif text[0] != text[-1]:
        return False
    else:
        text = text[1:-1]
        return is_palindrome(text, True)
        
user_string = input("Type your text here: ")
is_pal = is_palindrome(user_string)
if is_pal:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")