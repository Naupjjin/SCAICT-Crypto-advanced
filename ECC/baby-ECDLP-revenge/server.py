from sage.all import *
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import random

iv=os.urandom(32)

class Point:
	def __init__(self,x,y,p):
		F = GF(p)
		self.x = F(x)
		self.y = F(y)
		self.modulus = p

def addition(p1 : Point, p2: Point, a,b):
	x1 = p1.x
	x2 = p2.x
	y1 = p1.y
	y2 = p2.y

	if x1 == x2 and y1 == y2:
		lamda = (3*x1**2 + a) / (2*y1)
	else:
		lamda = (y2 - y1) / (x2 - x1)
	x = lamda**2 - x1 - x2
	y = lamda*(x1 - x) - y1
	return Point(x,y,p1.modulus)

def scalar_multiplication(p: Point, n,a,b):
	q = p
	r = 0
	while n > 0:
		if n % 2 == 1:
			try:
				r = addition(r,q,a,b)
			except:
				r = q
		q = addition(q,q,a,b)
		n = n//2
	return r 

def encrypt_flag(shared_secret: int):
    FLAG=b'CryptoADV{Fake_Flag}'
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))

    data = {}
    data['iv'] = iv.hex()
    data['encrypted_flag'] = ciphertext.hex()
    return data


nbits = 64
pbits = 256

# 定義橢圓曲線
p = 99061670249353652702595159229088680425828208953931838069069584252923270946291 #p bits=256
a = 1
b = 4

#生成點
g_x = 43190960452218023575787899214023014938926631792651638044680168600989609069200
g_y = 20971936269255296908588589778128791635639992476076894152303569022736123671173
G = Point(g_x, g_y, p)
print(f"G=({G.x},{G.y})")

#兩人的私鑰
n_a=random.getrandbits(nbits)
n_b=random.getrandbits(nbits)

#光的公鑰
public_A=scalar_multiplication(G , n_a , a , b)
print(f"public_A=({public_A.x},{public_A.y})")

#對立的公鑰
public_B=scalar_multiplication(G , n_b , a , b)
print(f"public_B=({public_B.x},{public_B.y})")

#兩人的密鑰
Secret_Key = scalar_multiplication(public_B , n_a , a , b)
ENC=encrypt_flag(Secret_Key.x)

print(ENC)

