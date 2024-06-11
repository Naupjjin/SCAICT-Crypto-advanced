from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

def decrypt_flag(shared_secret: int, iv: bytes, ciphertext: bytes):

    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.decrypt(pad(ciphertext, 16))
    print(ciphertext)

p = 310717010502520989590157367261876774703
a = 2
b = 3
E = EllipticCurve(GF(p),[a,b])

g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = E(g_x, g_y)

b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = E(b_x, b_y)

publickey=E(31175998738276450049303253119119683273,136193968131255250656172485538862928319)

n_a=G.discrete_log(publickey)
print("n_a=",n_a)

b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = E(b_x, b_y)

secret=B*n_a

iv=bytes.fromhex('619577def89cf5f3c6666c07fb6dff15') 
c=bytes.fromhex('0032e10e11df1f0595135684454745dd4bc4fe59488b504ce0e5c967ca8ea009d1367c3284ae458a3feade54fa07ab60')

decrypt_flag(secret.xy()[0] ,iv,c)