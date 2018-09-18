N=1500000

nl=[]
for i in range(N+1):
    nl+=[0]

def gcd(a, b):
    while b:
        a, b=b, a%b
    return a

mr=int((N/2)**0.5)+1
for m in range(1,mr):
    for n in range(1+m%2,m,1+m%2):
        if gcd(m,n)==1:
            m2=m*m
            n2=n*n
            a,b,c=m2-n2,2*m*n,m2+n2
            t=a+b+c
            p=1
            while p*t<=N: 
                nl[p*t]+=1
                p+=1
            

c=0     
for i in range(N+1):
	if nl[i]==1:
		c+=1

print(c)
