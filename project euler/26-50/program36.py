##completely brute force :(

import time
t=time.time()

def pallen(n,b=0):
    n=str(n)
    if b==2:
        n=n[2:]
    x=len(n)
    for i in range(x//2):
        if n[i]!=n[x-1-i]:
            return False
    return True
sm=0
for i in range(1,1000000,2):
    if pallen(i) and pallen(bin(i),2):
        sm+=i

print(sm)

print(time.time()-t)

