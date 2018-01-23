def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

prime=tuple(sieve(1000000))
n=2
const=4
count=0
while True:
    tn=n
    scount=0
    for i in prime:
        if tn%i==0:
            scount+=1
        while tn%i==0:
            tn//=i
        if scount>const:
            if count>2:
                print(count)
            count=0
            break
        if tn==1:
            if const!=scount:
                if count>2:
                    print(count)
                count=0
                break
            if scount==const:
                count+=1
                break
    if n%1000==0:
        print(n)
    if count==const:
        print(n-const+1)
        break
    n+=1
