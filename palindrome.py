def is_palindrome(text):
    clean_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    is_pal = True

    for character in text:
        if character.lower() in alphabet:
            clean_text += character.lower()

    # for test_char in clean_text[0:int(len(clean_text)/2)]:
    #     if test_char != clean_text[(clean_text.index(test_char)+1)*-1]:
    #         is_pal = False
    
    i=0
    while is_pal and i<(len(clean_text)/2):
        if clean_text[i] != clean_text[(i+1)*(-1)]:
            is_pal = False
        i+=1
    return is_pal
        
user_string = input("Type your text here: ")
is_pal = is_palindrome(user_string)
if is_pal:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")