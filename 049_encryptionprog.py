import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

# print(chars)

chars_list = list(chars)


key = chars_list.copy()
random.shuffle(key)

print(f"char: {chars_list}")
print(f"keys: {key}")

# encryption
plain_text = input("Enter a message to encrypt: ")


index_plain = [chars_list.index(letter) for letter in plain_text]

cipher_index = [key[index] for index in index_plain]

print(index_plain)
print(cipher_index)

cipher_text = "".join(cipher_index)

print(f"Original message: {plain_text}")
print(f"Cipher text: {cipher_text}")

# decryption
encrypted_text = input("Enter a message to decrypt: ")

index_encr = [key.index(letter) for letter in encrypted_text]

plain_index = [chars_list[index] for index in index_encr]

decipher_text = "".join(plain_index)

print(decipher_text)






# for letter in plain_text:
#     print(chars_list.index(letter))

    # print(letter, end = "")
