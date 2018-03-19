from time import time
t=time()

def bounce(n):
    inc=False
    dec=False
    f=n%10
    n//=10
    while n>0:
        l=f
        f=n%10
        n//=10
        if f>l:
            inc=True
        if f<l:
            dec=True
        if inc and dec:
            return True
    return inc and dec


n=1
b=0
i=1
while n<=10**7:
    n+=1
    if not bounce(n):
        b+=1
    if n%10**i==0:
        i+=1
        print (b)

print(time()-t)
