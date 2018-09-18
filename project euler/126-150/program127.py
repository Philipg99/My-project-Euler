## 23min execution time 
from time import time as t
w=t()
n=120000
l=[]
for i in range(n+1):
    l+=[set([])]


for i in range(2,n+1):
    if len(l[i])==0:
        for j in range(i,n+1,i):
            l[j].add(i)


pr=[1,1]
for i in range(2,n+1):
    p=1
    for j in l[i]:
        p*=j
    pr+=[p]


def rad(a,b):
    p=pr[a]*pr[b]*pr[a+b]
    if p<(a+b):
        return True
    return False

def co(a,b):
    if l[a]==l[a]-l[b]-l[a+b]:
        if l[b]==l[b]-l[a+b]:
            return True
    return False
s=0
for i in range(1,int(n/2)):
    for j in range(i+1,n-i+1,1+(1+i)%2):
        if rad(i,j):
            if co(i,j):
                print(i,j,i+j,s)
                s+=i+j

print(s)
print(t()-w)
