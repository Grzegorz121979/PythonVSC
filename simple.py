import random
import string

chars = string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(chars)
print(key)