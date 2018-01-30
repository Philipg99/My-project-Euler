import time
t=time.time()

memo=[-1]*10000000
fact=[0]*10

for i in range(10):
    f=1
    for j in range(1,i+1):
        f*=j
    fact[i]=f

## end of pre calculation
    
def numf(n):
    n=list(map(int,str(n)))
    s=0
    for i in n:
        s+=fact[i]
    return s
## main loop
count=0
for i in range(1000000):
    if i%100000==0:
        print(i,time.time()-t)
    l=[i]
    m=0
    while numf(i) not in l:
        if memo[i]>=0:
            m=memo[i]
            break
        i=numf(i)
        l+=[i]

    memo[l[0]]=len(l)+m-1 ## memoisation, poor implemantation
    
    if (len(l)+m)==60:
        count+=1
    
print(count)
print(time.time()-t)
