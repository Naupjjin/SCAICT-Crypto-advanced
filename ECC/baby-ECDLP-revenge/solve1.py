from sage.all import *
p = 99061670249353652702595159229088680425828208953931838069069584252923270946291
a = 1
b = 4
E = EllipticCurve(GF(p), [a,b])
G=E(43190960452218023575787899214023014938926631792651638044680168600989609069200 , 20971936269255296908588589778128791635639992476076894152303569022736123671173)
factor(G.order())
