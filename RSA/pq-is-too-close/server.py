from Crypto.Util.number import *
import gmpy2

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

msg = b"CryptoADV{Fake_flag}"
m = bytes_to_long(msg)

p = getPrime(512)
q = gmpy2.next_prime(p)
n=p*q
e=65537

print("n= ", n)
print("e= ", e)
print("c= ", encrypt(m,e,n))
