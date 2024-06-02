import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secret import FLAG, sourcecode
import base64

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


def main():
    print("-"*30)
    print("easy bit flipping")
    print("-"*30)
    while True:
        print("1->encrypt | 2->decrypt and check | 3->source code")
        number=int(input())
        if number==1:
            plaintext = "ABCDEFGHIJKLMNOP1234567890abcdef"

            ciphertext = encrypt_cbc(plaintext)
            print(f"Ciphertext: {base64.b64encode(ciphertext)}")
            print(f"iv: {base64.b64encode(iv)}")

        elif number==2:
            
            CIPHER=bytes.fromhex(input("Your Cipher= ").strip())
            decrypted_plaintext = decrypt_cbc(CIPHER)
            print(f"plaintext: {decrypted_plaintext}")


            if decrypted_plaintext[0]=='H':
                print('success!')
                print(FLAG)

            else:
                print('failed')
        
        elif number==3:
            print('source code:')
            print('-'*30)
            print(sourcecode)
            print('-'*30)
        else:
            exit()


try:
    main()

except:
    print("error!")
    exit()
