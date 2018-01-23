def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

prime=list(sieve(100000))
lon=len(prime)

                    
def bins(x,n):
    high=lon-1
    low=0
    while high>=low:
        mid=int((high+low)/2)
        if x[mid]==n:
            return True
        if x[mid]>n:
            high=mid-1
        if x[mid]<n:
            low=mid+1
    return False

for i in range(9,100000,2):
    if bins(prime,i)==False:
        check=0
        for j in prime:
            if j>i:
                break
            sq=(i-j)/2
            if sq**0.5==int(sq**0.5):
                check=1
                break
        if check==0:
            print (i)
            break
