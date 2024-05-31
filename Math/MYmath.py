
import functools
from Crypto.Util.number import *
from gmpy2 import *


def crt(c, n):
    '''
    Input: [c_1, ... c_i], [n_1, ..., n_i]
        x = c_1 (mod n_1)
        x = c_2 (mod n_2)
        ...
        x = c_n (mod n_i)
    Output: x
    '''
    N_ALL = functools.reduce(lambda x, y: x * y, n)
    total = 0

    for Ai, ni in zip(c, n):
        Ni = N_ALL // ni
        total += Ai * Ni * (gmpy2.gcdext(Ni, ni)[1] % ni)

    return total % N_ALL

def gcd(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

def GCDEXT(a,b):
    GCDNUM, y, x = gcdext(a,b)
    return (GCDNUM, y, x)