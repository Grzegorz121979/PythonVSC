'''
exercise coding string
'''
import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)

plain_text = input("Enter a message: ")


def cod_string(text, ch, k):
    '''
    function to coding string
    '''
    cipher_text = ""

    for letter in text:
        index = ch.index(letter)
        cipher_text += k[index]
    
    return cipher_text

print(f"The coded text is: {cod_string(plain_text, chars, key)}")

cipher_text = input("Enter a message: ")


def decod_string(text, ch, k):
    '''
    function to decoding string
    '''
    plain_text = ""

    for letter in cipher_text:
        index = k.index(letter)
        plain_text += ch[index]
    
    return plain_text

print(f"The decoded text is: {decod_string(cipher_text, chars, key)}")
