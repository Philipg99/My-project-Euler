from time import time as t
w=t()
def fsum(n):
    s=1
    i=1
    while n>1:
        tmp=1
        i+=1
        c=1
        while n%i==0:
            n//=i
            c*=i
            tmp+=c
        s*=tmp
    return s
    

def pn(n,phi):
    
    if len(phi)>n:
        if phi[n]!=-1:
            return phi[n]
    else:
        for i in range(len(phi),n+1):
            phi+=[-1]

    phi[n]=fsum(n)
    return phi[n]

phi=[0,1]
p=[1,1]

def calp(n,p):
    s=0
    for i in range(0,n):
        s+=pn(n-i,phi)*p[i]
    s//=n
    p+=[s]

k=1
while p[k]%1000000!=0:
    k+=1
    calp(k,p)
    if k%100==0:
        print(k)


print(k)
print(t()-w)
