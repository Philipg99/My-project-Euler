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
def d(n): ##checked
    r=[1]
    for prime in x:
        if prime<=n/prime:
            if n%prime==0:
                n//=prime
                if n%prime==0:
                    return [-1]
                nr=[]
                for i in r:
                    nr+=[i*prime]
                r+=nr
        else:
            break

    return r


                    
def bins(x,n):
    high=lon-1
    low=0
    while low<=high:
        mid=int((high+low)/2)
        if x[mid]==n:
            return True
        if x[mid]>n:
            high=mid-1
        if x[mid]<n:
            low=mid+1
    return False
    

def isprime(fact,n):
    for f in fact:
        if f <0:
            return False
        tc=int(f+n/f)
        if bins(x,tc)==False:
            return False
    return True

                     
#### init           
tte=time.time()
print(len(x))
track=0
total=0
####
                     
for i in x:

                     
    track+=1
    if track%10000==0:
        print(track,time.time()-tte)

                     
    fact=d(i-1) 
    if isprime(fact,i-1):
        total+=(i-1)
print(total,time.time()-t)
        
##funtionaly correct , time un optimezed , update time 30+174.2 seconds
