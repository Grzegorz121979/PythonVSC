"""
coding and decoding string exercise
"""
import random
import string

CHARS = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(CHARS)
key = chars.copy()
random.shuffle(key)

plain_text = input("Enter a message: ")


def cod_string(text, char_list, k):
    """
    coding string
    """
    c_text = ""

    for letter in text:
        index = char_list.index(letter)
        c_text += k[index]
    return cipher_text

print(f"The coded text is: {cod_string(plain_text, chars, key)}")

cipher_text = input("Enter a message: ")


def decod_string(text, char_list, k):
    """
    decoding string
    """
    p_text = ""

    for letter in text:
        index = k.index(letter)
        p_text += char_list[index]
    return plain_text

print(f"The decoded text is: {decod_string(cipher_text, chars, key)}")
