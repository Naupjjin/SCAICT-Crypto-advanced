from Crypto.Util.number import *

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

msg = b"Secret"
m = bytes_to_long(msg)

p=getPrime(100)
q=getPrime(100)
n=p*q
e=65537

print(encrypt(m,e,n))
