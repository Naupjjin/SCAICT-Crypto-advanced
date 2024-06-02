import gmpy2
import functools
from Crypto.Util.number import *

n0 = 0
c0 = 0
n1 = 0
c1 = 0
n2 = 0
c2 = 0
e = 0

def crt(a, m):
    prod, total = functools.reduce(lambda x, y: x * y, m), 0
    for ai, mi in zip(a, m):
        Mi = prod // mi
        total += ai * Mi * (gmpy2.gcdext(Mi, mi)[1] % mi)
    return total % prod

c = crt([c0, c1, c2], [n0, n1, n2])
m, _ = gmpy2.iroot(c, e)
print(long_to_bytes(m))