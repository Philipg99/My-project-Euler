import time
t1 = time.time()


def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
x= list(sieve(100000000))
print("post")
y=list(sieve(10000))
lon=len(x)



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
    

def sides(n,i):
    n=str(n)
    i=str(i)
    n1=int(n+i)
    n2=int(i+n)

    if bins(x,n1) and bins(x,n2):
        return True
    return False

dic={}

for i in y:
    for k in dic:
        if sides(k,i):
            dic[k]+=[i]
    dic[i]=dic.get(i,[])
        



for i in dic:
    for j in dic[i]:
        for k in dic[j]:
            if k in dic[i]:
                for l in dic[k]:
                    if l in dic[j] and l in dic[i]:
                        for m in dic[l]:
                            if m in dic[k] and m in dic[j] and m in dic[i]:
                                print(i,j,k,l,m,i+j+k+l+m)

            

print(time.time()-t1)
