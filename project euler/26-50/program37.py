#sive limit was set after learning the answer

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
x= list(sieve(1000000))
print(time.time()-t)
lon=len(x)

def bins(x,n):
    high=lon-1
    low=0
    while high>=low:
        mid=(high+low)//2
        if x[mid]==n:
            return True
        if x[mid]>n:
            high=mid-1
        if x[mid]<n:
            low=mid+1
    return False
    
sm=0
for prime in x :
    flg=0
    if prime >10:
        prime=str(prime)
        for i in range(1,len(prime)):
            if bins(x,int(prime[:i]))==False or bins(x,int(prime[len(prime)-i:]))==False:
                flg=1

                
        if flg==0:
            sm+=int(prime)
            print(prime,prime[:i],prime[len(prime)-i:])

print(sm)
            


