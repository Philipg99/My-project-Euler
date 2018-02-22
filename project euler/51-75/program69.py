##prime product while under a million

import time
t=time.time()
def gcd(a, b):
    while b:
        a, b=b, a%b
    return a
def phi(a):
    b=a-1
    c=0
    while b:
        if gcd(a,b)==1:
            c+=1
        b-=1
    return c
mf=1000
mi=0
for i in range(2,1000001):
    f=phi(i)/i
    if f<mf:
        mf=f
        mi=i
        print(mi,mf,time.time()-t)
    if i%1000==0:
        print(i,time.time()-t)
print(mi,mf,time.time()-t)
print(time.time()-t)

            
