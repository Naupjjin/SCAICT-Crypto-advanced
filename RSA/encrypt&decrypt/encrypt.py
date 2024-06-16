from Crypto.Util.number import *

def encrypt(m,e,n):
    c=pow(m,e,n)
    return c

msg = b"CryptoADV{Have_p_q_can_decrypt_easy!}"
m = bytes_to_long(msg)

p=getPrime(1024)
q=getPrime(1024)
n=p*q
e=65537

print("n= ", n)
print("p= ", p)
print("q= ", q)
print("e= ", e)
print("c= ", encrypt(m,e,n))
