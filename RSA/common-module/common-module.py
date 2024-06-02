from gmpy2 import gcdext
from Crypto.Util.number import *

n = 0
c1 = 0
c2 = 0
e1 = 0
e2 = 0
_, t, u = gcdext(e1, e2)
m = pow(c1, t, n) * pow(c2, u, n) % n
print(long_to_bytes(m))