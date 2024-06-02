plaintext = "ABCDEFGHIJKLMNOP1234567890abcdef"
ciphertext = 
IV = bytearray(ciphertext[:16])
C = ciphertext[16:]

#IV[0] = IV[0] ^ ord(plaintext[0]) ^ ord('H')
IV[0] = IV[0] ^ ord(plaintext[0]) ^ ord('H')

CIPHER = bytes(IV) + C
print(CIPHER)