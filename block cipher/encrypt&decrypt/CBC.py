from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

def encrypt_cbc(plaintext, key):

    iv = get_random_bytes(AES.block_size)
    
   
    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)

    return iv + ciphertext

def decrypt_cbc(ciphertext, key):

    iv = ciphertext[:AES.block_size]

    actual_ciphertext = ciphertext[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_padded_plaintext = cipher.decrypt(actual_ciphertext)
    
       
    return decrypted_padded_plaintext

key = os.urandom(16) 
plaintext = "Hello, world!"

ciphertext = encrypt_cbc(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_plaintext = decrypt_cbc(ciphertext, key)
print(f"Decrypted: {decrypted_plaintext}")
