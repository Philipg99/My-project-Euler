import time
t= time.time()
def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
x= set(sieve(10000000))
ncirc=4
count=0
print(len(x))
def precheck(n):
    n=list(map(int,str(n)))
    if sum(n)%3==0 or 5 in n:
        return False
    for l in n:
        if l%2==0:
            return False
    return True
    
def rot(n):
    f=n%10
    pre=n
    pre//=10
    pre=f*10**(len(str(pre)))+pre
    while pre!=n:
        if pre not in x:
            return False
        f=pre%10
        pre//=10
        pre=f*10**(len(str(pre)))+pre
    return True
        
    
    

for prime in x:
    if precheck(prime):
        if rot(prime):
            ncirc+=1
    



print (ncirc)        
print(time.time()-t)
