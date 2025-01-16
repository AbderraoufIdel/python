import string

def is_pangram(sentence):

    lowercase_alphabet = string.ascii_lowercase

    sentence = sentence.lower()

    #remove all the non alphabetic characters
    sentence = ''.join(c for c in sentence if c.isalpha())

    return set(sentence) == set(lowercase_alphabet)

print(is_pangram("abcdefghijklmnopqrstuvwxyz"))