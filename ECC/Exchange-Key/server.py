from sage.all import *
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

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
    FLAG=b'CryptoADV{Key_Exachange_can_generate_one_secret_key!!!!!}'
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



G= Point(1804,5368,9739)
n_a=5741
n_b=3478
print("G=(1804,5368)")
print("n_a=",n_a)
print("n_b=",n_b)

Q_A=scalar_multiplication(G,n_a,497,1768)
Q_B=scalar_multiplication(G,n_b,497,1768)

Secret_Key=scalar_multiplication(Q_A,n_b,497,1768)

ENC=encrypt_flag(Secret_Key.x)

print(ENC)