import time
t= time.time()

a=b=n=1

while a<10**999:
    a,b=b,a+b
    n+=1
print (n)
print (time.time()-t)
