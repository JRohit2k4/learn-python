import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(keys)

#ENCRYPT
plain_text = input("Enter message to encrypt: ")
cipher_text = ""

for letter in plain_text:
  index = chars.index(key)
  cipher_text += key[index]
print(f"Original text = {plain_text}")
print(f"Encrypted text = {cipher_text}")

#DECRYPT
cipher_text = input("Enter encrypted message: ")
plain_text = ""

for letter in cipher_text:
  index = key.index(char)
  plain_text += char[index]
print(f"Encrypted text = {cipher_text}")
print(f"Original text = {plain_text}")
