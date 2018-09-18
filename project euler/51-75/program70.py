from time import time as ta
wa=ta()
n=10**7
l=[]
for i in range(n+1):
    l+=[[]]


for i in range(2,n+1):
    if len(l[i])==0:
        for j in range(i,n+1,i):
            l[j]+=[i]

print('start')

def toi(n,l):
    p=n
    for i in l[n]:
        p*=(1-1/i)
    return int(p)

def comp(i,p):
    i=list(str(i))
    p=list(str(p))
    i.sort()
    p.sort()
    if len(p)==len(i):
        for j in range(len(i)):
            if p[j]!=i[j]:
                return False
        return True
    return False

s=10
maxn=0
for i in range(2,n+1):
    p=toi(i,l)
    if comp(i,p):
        t=i/p 
        if t<s:
            s=t
            maxn=i


print(maxn,s)

print(ta()-wa)
