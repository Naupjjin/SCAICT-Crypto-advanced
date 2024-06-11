from sage.all import *
p = 9739
a = 497
b = 1786
E = EllipticCurve(GF(p), [a,b])
P=E(3596, 7399)
print(P.order())