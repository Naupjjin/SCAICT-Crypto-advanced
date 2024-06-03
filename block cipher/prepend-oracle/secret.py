FLAG=b'CryptoADV{brute_force_is_a_good_civilization?}'
sourcecode='''
import os
from Crypto.Cipher import AES
from secret import FLAG, sourcecode

KEY = os.urandom(16)


def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    print("1 -> source code | 2 -> encrypt")
    choose=int(input())
    if choose==1:
        print("-"*30)
        print(sourcecode)
        print("-"*30)
    elif choose==2:
        aes = AES.new(KEY, AES.MODE_ECB)
        
        while True:
            message = bytes.fromhex(input('message = ').strip())
            cipher = aes.encrypt(pad(message + FLAG))
            print(f'cipher = {cipher.hex()}')
    else:
        exit()

try:
    main()
except:
    print("error...")
    exit()

'''