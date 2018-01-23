import time
t= time.time()
n=1

for i in range(2,100):
    n*=i
total = sum(list(map(int,list(str(n)))))
print (total)
print(time.time()-t)
