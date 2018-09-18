from math import *

def su(m):
    s=0
    while m>0:
        s+=m%10
        m//=10
    return s


l=[]
for i in range(2,199):
    p=i
    if p==10 or p==100:
        continue
    while p<10**22:
        n=log(p,su(p))
        if abs(round(n)-n)<0.001:
            if p>10 and p not in l:
                l+=[p]
        p*=i

l.sort()
print(l[30])
        

