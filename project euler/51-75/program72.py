from time import time as t
w=t()

l=[]
for i in range(1000001):
    l+=[[]]


for i in range(2,1000001):
    if len(l[i])==0:
        for j in range(i,1000001,i):
            l[j]+=[i]

def toi(n,l):
    p=n
    for i in l[n]:
        p*=(1-1/i)
    return int(p)
print('start')
s=0
for i in range(2,10**6+1):
    s+=toi(i,l)

print(s)

print(t()-w)
