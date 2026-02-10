import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]

print("Original message: " + plain_text)
print("Encrypted message: " + cipher_text)


# DECRYPT
original_text = input("Enter a message to decrypt: ")
decrypted_text = ""

for char in original_text:
    index = key.index(char)
    decrypted_text += chars[index]

print("Original message: " + original_text)
print("Decrypted message: " + decrypted_text)
