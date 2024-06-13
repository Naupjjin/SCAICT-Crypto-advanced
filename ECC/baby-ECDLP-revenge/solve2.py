from Crypto.Cipher import AES
from Crypto.Util.number import inverse
from Crypto.Util.Padding import pad, unpad
from collections import namedtuple
from random import randint
import hashlib
from sage.all import *



p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
a = 1
b = 4
E = EllipticCurve(GF(p), [a,b])
G = E(43190960452218023575787899214023014938926631792651638044680168600989609069200 , 20971936269255296908588589778128791635639992476076894152303569022736123671173)
A = E(56315776141276215961585461938032715236547979801894402831501016927979992675300,31315140604927506098139810888178705595653236300187955665302014140786297231037)


orderG = G.order()

# 少取後兩個factor
factors = list(factor(orderG))[:-2]
m = 1
moduli = []
remainders = []
print(factors)

# pohlig-hellman
for i, j in factors:

    mod = i**j
    g2 = G*(orderG//mod)
    q2 = A*(orderG//mod)
    r = discrete_log(q2, g2, operation='+')
    remainders.append(r)
    moduli.append(mod)
    m *= mod

n_a = crt(remainders, moduli)
print("n_a:",n_a)

# 產生secret key
B=E(11354260993527690656381820295371596178140451292290500974231906071266047876139,72159291801897736241471580897828046849622443738486949249646879333653022349584)
secret=(B*n_a).xy()[0]

# 解密
sha1 = hashlib.sha1()
sha1.update(str(secret).encode('ascii'))
key = sha1.digest()[:16]

iv= bytes.fromhex('6d644e253c59797f08714ad1730866fb')
encrypted_flag=bytes.fromhex('624bfd0de56a5c9d6861b6052a630d0db3437009a3817cc36ea09ae950420af40e9f5ec42d85a916581d15bc6545dcbb114512c8b2abdc1afbd512e9c1b3c1db')

cipher = AES.new(key, AES.MODE_CBC, iv)
m=cipher.decrypt(pad(encrypted_flag, 16))

print(m)