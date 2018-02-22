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
                
x= list(sieve(10000000))

lon=len(x)

def bins(x,n):
    for prime in x:
        if n%prime==0:
            return False
        if prime**2>n:
            return True
    

s=1
d1=[1,1,0,4]
d2=[1,1,0,2]
while ((d1[2]+ d2[2])/(d1[1]+d2[1]-1)>0.1) or s<2422:

    for i in range(2):
        d1[0]+=d1[3]
        if bins(x,d1[0]):
            d1[2]+=1

    d1[1]+=2
    d1[3]+=4

    for i in range(0,3,2):    
        d2[0]+=d2[3]+i
        if bins(x,d2[0]):
            d2[2]+=1

    d2[1]+=2
    d2[3]+=4

    s+=2 

    if (s-1)%1000==0:
        print(s,(d1[2]+ d2[2])/(d1[1]+d2[1]-1))
    
print(s,d1,d2)
print(time.time()-t)









    
