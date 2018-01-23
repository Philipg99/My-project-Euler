import time
t=time.time()
total=0
for i in range(1,1001):
    total+=i**i
print (total%10**10)
print (time.time()-t)
