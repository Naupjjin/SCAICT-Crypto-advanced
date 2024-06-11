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

# 定義橢圓曲線
p = 310717010502520989590157367261876774703
a = 2
b = 3

#生成點
g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = Point(g_x, g_y, p)
print(f"G=({G.x},{G.y})")

#光的私鑰
n_a=random.randint(1, p)

#光的公鑰
public_A=scalar_multiplication(G , n_a , a , b)
print(f"public_A=({public_A.x},{public_A.y})")

#對立的公鑰
b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
public_B = Point(b_x, b_y ,p)

#兩人的密鑰
Secret_Key = scalar_multiplication(public_B , n_a , a , b)
ENC=encrypt_flag(Secret_Key.x)

print(ENC)

