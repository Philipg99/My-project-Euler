from itertools import product
from time import time
t=time()

def ssq(n):
    return n*(n+1)*(2*n+1)/6
def sr(b,e):
    return ssq(e)-ssq(b)
  
c=0
pal=[]
i=[0,0,0,0]
for i[0],i[1],i[2],i[3] in product(range(10),repeat=4):
    i=list(map(str,i))
    p=len(i)
    b=''
    for x in range(p):
        if x==(p-1):
            if int(b)==0:
                b=''
            else:
                while int(b[0])==0:
                    b=b[1:]
            n1=int(b+i[x]+b[::-1])
            n2=int(b+i[x]*2+b[::-1])
            break
        b=b+i[x]
    if n1!=0:
        pal+=[n1,n2]
pal.sort()
pal=pal[1:]
s=0
for p in pal:
    b=0
    e=1
    while sr(b,e)<p:
        e+=1
    while e-b>1:
        while sr(b,e)<p:
            e+=1
        while sr(b,e)>p:
            b+=1
        if p==(sr(b,e))and e-b>1:
            print(p,b,e,time()-t)
            s+=p
            break

print(s)
print(time()-t)
