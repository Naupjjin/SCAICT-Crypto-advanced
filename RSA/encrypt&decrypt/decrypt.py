from Crypto.Util.number import *
import gmpy2
p= 0
q= 0
e = 65537
c = 0
n=p*q
phi = (q - 1) * (p - 1)
d = gmpy2.invert(e , phi)

print(long_to_bytes(pow(c , d , n)))