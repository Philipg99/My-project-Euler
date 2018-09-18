def p3(n):
    return int(n*(n+1)/2)
def p4(n):
    return n*n
def p5(n):
    return int(n*(3*n-1)/2)
def p6(n):
    return n*(2*n-1)
def p7(n):
    return int(n*(5*n-3)/2)
def p8(n):
    return n*(3*n-2)

f=[p3,p4,p5,p6,p7,p8]

pr3={}
pr4={}
pr5={}
pr6={}
pr7={}
pr8={}
pr=[pr3,pr4,pr5,pr6,pr7,pr8]
for pre in pr:
    for i in range (10,100):
        pre[i]=[]
    
p=0
for fun in f:
    n=1
    while fun(n)<1000:
        n+=1
    while fun(n)<10000:
        if fun(n)%100>=10:
            pr[p][int(fun(n)%100)]+=[fun(n)]
        n+=1

    p+=1

for j in range(6):
	for i in range(10,100):
		if len(pr[j][i])!=0:
			print(i,pr[j][i])
	print('\n')
