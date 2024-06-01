from Crypto.Util.number import *
import gmpy2
p = getPrime(512)
q = gmpy2.next_prime(p)
n=p*q
print(p)
print(q)
print(n)
 
temp=gmpy2.iroot(n,2)[0]  
p=gmpy2.next_prime(temp)
q=n//p
print(p)
print(q)