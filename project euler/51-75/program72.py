##fundamentaly broken

import time
t = time.time()


r=10
a = [[]]
for i in range(r):
    a+=[[]]
for i in range(2,r+1):
    j=1##one to incldue it self
    while j*i<r+1:
        a[j*i]+=[i]
        j+=1
print(time.time()-t)
##for i in range(len(a)):
##    print(i,a[i])

for i in range(2,len(a)):
    x=len(a[i])
    phi=i-x
    print(i,phi,i/phi,a[i])
    

print(time.time()-t)
