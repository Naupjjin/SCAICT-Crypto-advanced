from Crypto.Util.number import *

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

msg = b"CryptoADV{Fake_Flag}"
m = bytes_to_long(msg)

p=getPrime(50)
q=getPrime(50)
n=p*q
e=65537

print("n= ", n)
print("p= ", p)
print("q= ", q)
print("e= ", e)
print("c= ", encrypt(m,e,n))
