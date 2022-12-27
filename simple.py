import random
import string

plain_text = input("Enter a message: ")

def cod_string(plain_text):
    chars = " " + string.ascii_letters + string.punctuation + string.digits
    chars = list(chars)
    key = chars.copy()

    random.shuffle(key)
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    
    return cipher_text

print(plain_text)
coding_string = cod_string(plain_text)
print(coding_string)