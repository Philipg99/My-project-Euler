
def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
l= list(sieve(10000))


n=50000000

n2=list(map(lambda x : x**2,[x for x in l if x<(n**(1/2))]))
n3=list(map(lambda x : x**3,[x for x in l if x<(n**(1/3))]))
n4=list(map(lambda x : x**4,[x for x in l if x<(n**(1/4))]))

c=set([])

for i in n4:
    for j in n3:
        if i+j>n:
            break
        for k in n2:
            if i+j+k<n:
                c.add(i+j+k)
            else:
                break
                
            
print(len(c))
    

