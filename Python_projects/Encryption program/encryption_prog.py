import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

#ENCRYPT
plain_text = input("Enter message to encrypt: ")
cipher_text = ""

for letter in plain_text:
  index = chars.index(key)
  cipher_text += key[index]
print(f"Original text = {plain_text}")
print(f"Encrypted text = {cipher_text}")
