'''
exercise coding string
'''
import random
import string

plain_text = input("Enter a message: ")


def cod_string(text):
    '''
    function to coding string
    '''
    chars = " " + string.ascii_letters + string.punctuation + string.digits
    chars = list(chars)
    key = chars.copy()

    random.shuffle(key)
    cipher_text = ""

    for letter in text:
        index = chars.index(letter)
        cipher_text += key[index]
    
    return cipher_text

print(f"The orgilan text is: {plain_text}")
coding_string = cod_string(plain_text)
print(f"The coded text is: {coding_string}")