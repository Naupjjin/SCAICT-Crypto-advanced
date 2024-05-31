
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def encrypt_ecb(plaintext, key):

    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)

    ciphertext = cipher.encrypt(padded_plaintext)
    
    return ciphertext

def decrypt_ecb(ciphertext, key):
 
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)

    
    return decrypted_padded_plaintext


key = os.urandom(16)
plaintext = 'This is a ciphertext. OuO, Secret!Secret!Secret!'


ciphertext = encrypt_ecb(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_plaintext = decrypt_ecb(ciphertext, key)
print(f"Decrypted: {decrypted_plaintext}")
