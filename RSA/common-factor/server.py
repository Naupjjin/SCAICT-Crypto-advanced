from Crypto.Util.number import *

FLAG = b'CryptoADV{Fake_flag}'

p  = getPrime(512)
q1 = getPrime(512)
q2 = getPrime(512)
n1 = p * q1
n2 = p * q2
e = 65537

m = bytes_to_long(FLAG)
c = pow(m, e, n1)
print(f'n1 = {n1}')
print(f'n2 = {n2}')
print(f'e = {e}')
print(f'c = {c}')