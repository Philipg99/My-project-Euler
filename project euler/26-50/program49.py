def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

s=list(sieve(10000))
lst=[i for i in s if i>1000]
print (len(lst))

def same(n,i):
    n=list(str(n))
    i=list(str(i))
    for h in n:
        if h in i:
            i.remove(h)
    if len(i)==0:
        return True
    else:
        return False

def condiff(temp):
    n=len(temp)
    for i in range(n):
        for j in range(i+1,n):
            d=temp[j]-temp[i]
            if temp[j]+d in temp:
                c=temp[j]
                print (c-d,c,c+d)
                return True
    return False

l=len(lst)


i=j=0
while i<l:
    temp=[lst[i]]
    j=i+1
    while j <l:
        if same(lst[i],lst[j]):
            temp+=[lst[j]]
            del lst[j]
            l-=1
        j+=1
    i+=1
    if len(temp)>3:
        condiff(temp)


            
