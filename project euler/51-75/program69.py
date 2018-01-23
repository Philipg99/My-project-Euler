###code not needed it is the product of all primes whos product is under 1000000


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



def d(n): ##checked
    r=[]
    for prime in x:
        if prime<=n and n%prime==0:
            while n%prime==0:
                n//=prime
            r+=[prime]

    return r


def phi(n):
    a=[True]*n
    a[0]=False
    for i in d(n):
        j=1
        while i*j<n:
            a[i*j]=False
            j+=1
    count=0
    for v in a:
        if v==True:
            count+=1

    return count

mx=0
n=0
for i in range(2,10001):
    if i/phi(i)>mx:
        mx=i/phi(i)
        n=i

print (mx,n)
print(time.time()-t)

            
