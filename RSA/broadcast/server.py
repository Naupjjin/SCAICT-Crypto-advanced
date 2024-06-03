from Crypto.Util.number import *
from secret import FLAG

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

def main():
    for i in range(5):
        print('1 -> encrypt | 2 -> source code | 3 -> exit' )
        choose=int(input("> "))
        if 
        m = bytes_to_long(FLAG)

        p=getPrime(2048)
        q=getPrime(2048)
        n=p*q
        e=3

        print('e=', e)
        print('n=', n)
        print('Cipher=',encrypt(m,e,n))


try:
    main()

except:
    print('exit')
    exit()