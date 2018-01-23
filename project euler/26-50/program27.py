def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
genb = sieve(1000)
tb=[x for x in genb]
b=[]
for t in tb:
    b+=[t,t*-1]
a=[x for x in range(-999,1000,2)]

def isprime(n):
    i=2

    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

ml=0
prod=0
for sb in b:
    for sa in a :
        tl=0
        for n in range(abs(sb)):
            tn=n**2+n*sa+sb
            if isprime(tn) and tn>0:
                tl+=1
            else:
                if tl>ml:
                    ml=tl
                    prod=sb*sa
                break
print (ml,prod)
