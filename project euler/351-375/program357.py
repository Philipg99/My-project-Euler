import time
t = time.time()
def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

x= tuple(sieve(1000000))
print(time.time()-t)
setx=set(x)
setn=set(range(2,1000000))
def d(n): ##need to fix this
    r=set([])
    for num in setn:
        if num**2>n:
            break
        if n%num==0:
            r|={num}
    return r

def isprime(tem,n):
    for i in tem:
        tc=int(i+n/i)
        if tc not in setx:
            return False
    return True
            
tte=time.time()
print(len(x))
track=0
total=0
for i in x:
    track+=1
    if track%10000==0:
        print(track,time.time()-tte)
    tem=d(i-1) 
    if isprime(tem,i-1):
        total+=(i-1)

print(total,time.time()-tte)
        
##funtionaly correct , time un optimezed
