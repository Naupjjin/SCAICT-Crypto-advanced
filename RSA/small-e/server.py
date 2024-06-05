from Crypto.Util.number import *

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

msg = b"CryptoADV{Fake_flag}"
m = bytes_to_long(msg)

p=getPrime(2048)
q=getPrime(2048)
n=p*q
e=3

print("n= ", n)
print("p= ", p)
print("q= ", q)
print("e= ", e)
print("c= ", encrypt(m,e,n))
