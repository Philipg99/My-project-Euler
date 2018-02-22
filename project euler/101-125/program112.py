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


n=100
b=0

while (b/n)!=(0.99):
    n+=1
    if bounce(n):
        b+=1
print(n)
print(time()-t)
