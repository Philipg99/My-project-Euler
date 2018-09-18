import time
t = time.time()
def sieve(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):    
                a[n] = False

num=10**8
x= list(sieve(num))

print(time.time()-t)

def bins(x,n):
    high=len(x)-1
    low=0
    while low<=high:
        mid=int((high+low)/2)
        if x[mid]==n:
            return mid
        if x[mid]>n:
            high=mid-1
        if x[mid]<n:
            low=mid+1
    return mid

n=0
c=0
while x[n]<=num**0.5:
    m=bins(x,num/x[n])
    if x[m]*x[n]>num:
        m-=1
    c+=len(x[n:m+1])
    n+=1

print(c)
    
print(time.time()-t)
