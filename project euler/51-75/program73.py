
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
    ret=[]
    for v in range(len(a)):
        if a[v]==True:
            ret+=[v]

    return ret
c=0
for i in range(2,12001):
    if i%100==0: print(i,time.time()-t)
    for j in phi(i):
        if j/i<1/2 and j/i>1/3:
            c+=1
print(c)
print(time.time()-t)

            
