import string

def rotate(text, key):
    alphabet= string.ascii_lowercase
    cipher = ""
    for x in text:
        if x.lower() in alphabet:
            anchor = alphabet.index(x.lower())
            new_anchor = (anchor + key) % len(alphabet) 
            cipher_char = alphabet[new_anchor]
            if x.isupper():
                cipher_char = cipher_char.upper()
            cipher += cipher_char
        
        else:
            cipher += x
    return cipher