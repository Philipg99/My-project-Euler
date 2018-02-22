import time
t=time.time()

def gcd(a, b):
    while b:
        a, b=b, a%b
    return a
def phi(a):
    b=a-1
    c=0
    while b:
        if gcd(a,b)==1:
            c+=1
        b-=1
    return c
n=2*3*4*5*6*7*11*13*17
f=1

while f>15499/94744:
    ft=phi(n)/n
    if ft<f:
        f=ft
        print('lowest',f)
    n+=1
    if n%500==0:
        print(n,'       ',time.time()-t)

print(time.time()-t)
