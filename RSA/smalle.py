from gmpy2 import *
from Crypto.Util.number import *

n= 0
e= 0
c= 0
flag = iroot(c, e)[0]


flag_bytes = long_to_bytes(flag)
print(flag_bytes)