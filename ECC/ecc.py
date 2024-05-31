from sage.all import GF
class Point:
	def __init__(self,x,y,p):
		F = GF(p) #定義有限域
		self.x = F(x) #讓x,y在有限域下運算
		self.y = F(y)
		self.modulus = p #模數

def addition(p1 : Point, p2: Point, a,b):
	x1 = p1.x
	x2 = p2.x
	y1 = p1.y
	y2 = p2.y
	if x1 == x2 and y1 == y2: #如果P,Q重合
		d = (3*x1**2 + a) / (2*y1) 
	else: #P和Q不同兩點
		d = (y2 - y1) / (x2 - x1)
	x = d**2 - x1 - x2
	y = d*(x1 - x) - y1
	return Point(x,y,p1.modulus)

#np->快速冪
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