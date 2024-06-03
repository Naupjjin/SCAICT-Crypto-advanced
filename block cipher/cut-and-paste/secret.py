FLAG=b'CryptoADV{Cut_and_paste_your_love}'
sourcecode='''
import os
from Crypto.Cipher import AES
from secret import FLAG, sourcecode

KEY=os.urandom(16)


def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    print('1 -> source code | 2 -> start | 3 -> exit')
    choose=int(input('> '))
    if choose == 1:
        print('-'*30)
        print(sourcecode)
        print('-'*30)
    elif choose == 2: 
        aes = AES.new(KEY, AES.MODE_ECB)  
        padding = input('padding= ').strip()
        if ':;' in padding:
            raise ValueError
        
        token =f'user:KasuganoSora;padding:{padding};favorability:0;'.encode()
        token = aes.encrypt(pad(token))
        print(f'token={token.hex()}')


        token = bytes.fromhex(input('token = ').strip())
        token = aes.decrypt(token)
        user,passwd, favorability,_ = token.split(b';')
        if int(favorability.split(b':')[1]) > 100000:
            YN=input("是否向穹妹告白?(Y/N)")
            if YN=="Y":
                print("我也喜歡悠……不會輸給任何人……")
                print(FLAG)
            else:
                print("內心的某處……在等待著悠。")
        else:
            print('悠挑選的換洗衣服，品味太差……而且那是什麼意思？還帶著裝醬油的瓶子，真是搞不懂……')

    else:
        exit()

try:
    main()
except:
    print('LOSE')
    exit()
'''