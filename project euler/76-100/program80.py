from decimal import *

getcontext().prec = 105

def sqr(n):
	n=Decimal(n)**(Decimal(1)/Decimal(2))
	return n
s=0
for i in range(2,100):
	if i not in [1,4,9,16,25,36,49,64,81,100]:
		x=str(sqr(i))[2:101]+str(sqr(i))[0:1]
		s+=(sum(list(map(int,str(x)))))

print(s)
