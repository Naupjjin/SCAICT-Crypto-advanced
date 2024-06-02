from math import gcd
from Crypto.Util.number import *

n1 = 0
n2 = 0
c = 0

n = n1
p = gcd(n1, n2)
q = n // p
e = 65537
d = inverse(e, (p - 1) * (q - 1))
m = pow(c, d, n)
print(long_to_bytes(m))