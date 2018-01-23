import time
t = time.time()
print (t)
def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
x= list(sieve(1000000))
t=0
f=[0]
for i in range(len(x)):
    t+=x[i]
    f.append(t)
n=len(x)
print('done')
ml=0
mp=0
flg=0
for i in range(n-1,-1,-1):
    print (i,ml,mp)
    for j in range(i-1,-1,-1):
        for k in range(j-1,-1,-1):
            if f[j]-f[k]==x[i]:
                if j-k>ml:
                    ml=j-k
                    mp=x[i]
            if f[j]-f[k]>x[i]:
                break
    if i-ml<0:
        break

print (ml,mp)
t2=time.time()

print (t2)
