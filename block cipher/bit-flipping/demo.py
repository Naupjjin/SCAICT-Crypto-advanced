import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

iv = os.urandom(16)
key = os.urandom(32)

def encrypt_cbc(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return iv + ciphertext

def decrypt_cbc(ciphertext):
    iv = ciphertext[:AES.block_size]
    actual_ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_plaintext = cipher.decrypt(actual_ciphertext)
    return unpad(decrypted_padded_plaintext, AES.block_size).decode()

plaintext = "ABCDEFGHIJKLMNOP1234567890abcdef"

ciphertext = encrypt_cbc(plaintext)
print(f"Encrypted: {ciphertext}")

IV = bytearray(ciphertext[:16])
C = ciphertext[16:]

IV[0] = IV[0] ^ ord(plaintext[0]) ^ ord('H')

CIPHER = bytes(IV) + C

decrypted_plaintext = decrypt_cbc(CIPHER)
print(f"Decrypted: {decrypted_plaintext}")


if decrypted_plaintext[0]=='H':
    print('success!')

else:
    print('failed')
