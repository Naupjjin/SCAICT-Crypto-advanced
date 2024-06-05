import random
from Crypto.Util.number import *

FLAG = b'CryptoADV{Fake_flag}'

p = getPrime(512)
q = getPrime(512)
n = p * q
e1 = 257
e2 = 65537

m = bytes_to_long(FLAG)
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
print(f'e1 = {e1}')
print(f'e2 = {e2}')
print(f'n = {n}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')