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

P = Point(493, 5564,9739)
Q = Point(1539, 4742,9739)
R = Point(4403,5202,9739)
x1 = addition(P,Q,497,1768)
x2 = addition(x1,P,497,1768)
x3 = addition(x2,R,497,1768)
x4 = addition(x3,P,497,1768)
x5 = addition(x4,Q,497,1768)
assert x5.y**2 == x5.x**3 + 497*x5.x + 1768 #確認所運算是否在E上
print(x5.x, x5.y)