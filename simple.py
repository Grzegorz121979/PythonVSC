sentence = "Hello World"
key = int(input("Enter a key: "))

def code_string(s, k):
    numbers = []
    letters = []
    code_s = ""
    
    for letter in s:
        numbers.append(ord(letter) + k)
        
    for number in numbers:
        letters.append(chr(number))
        
    i = 0
    
    while i < len(letters):
        code_s += letters[i]
        i += 1
    
    return code_s


def decode_string(s, k):
    numbers = []
    letters = []
    code_s = ""
    
    for letter in s:
        numbers.append(ord(letter) - k)
        
    for number in numbers:
        letters.append(chr(number))
        
    i = 0
    
    while i < len(letters):
        code_s += letters[i]
        i += 1
    
    return code_s

print(code_string(sentence, key))
print(decode_string(code_string(sentence, key), key))