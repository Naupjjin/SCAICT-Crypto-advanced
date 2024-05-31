
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
plaintext = '{name:naup96321;password:123456;role:user}'

#CryptoADV{Fake_f
#laf_try_to_do_de
#mo}

ciphertext = encrypt_ecb(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_plaintext = decrypt_ecb(ciphertext, key)
print(f"Decrypted: {decrypted_plaintext}")

for i in range(0,len(ciphertext),16):
    print(ciphertext[i:i+16])

