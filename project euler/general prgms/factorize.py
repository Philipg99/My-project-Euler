import time
t=time.time()
def d(n,f): ##need to fix this
    if n%2==0:
        sl=f[n//2]
        print('call in sp',n,n//2,f[n//2] )
        print (n)
        sl+=[x*2 for x in f[n//2]]
        sl=list(set(sl))
        print(sl)

        print(f[1],'65342790-')
        f[n]= sl
        return 0
    r=1
    sl=[]
    while r*r<=n:
        if r**2>=n:
            sl+=[r]
            break
        if n%r==0:
            sl+=[n//r]
            sl+=[r]
        r+=1
    sl=list(set(sl))
    print(sl)
    f[n]= sl
    return 0

f=[[0],[1]]+[None]*20
n0=0
for i in range(2,11):
    n0=d(i,f)



    
print('\n\n')
for d in f:
    print(d)
print (time.time()-t)
