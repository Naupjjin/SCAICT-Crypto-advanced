from Crypto.Util.number import *
import gmpy2
n=  652663280262364793463690101549
p=  753944542923139
q=  865664837538191
e=  65537
c=  268171184711408593973438485885

n=p*q
phi = (q - 1) * (p - 1)
d = gmpy2.invert(e , phi)

print(long_to_bytes(pow(c , d , n)))