from Crypto.Cipher import AES
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext.decode('ascii'))


shared_secret = 176
iv = '4abcc91c71293f536433b0c8727afb0d'
ciphertext = '9f035f0fdd41207121ce6ca44f33314803829170d77449151f9d068d2b51d1aaa6e2acd4279605d7bb99108e46c337c9329e5b930c334f5b47a33fc9e3c865ca'

print(decrypt_flag(shared_secret, iv, ciphertext))