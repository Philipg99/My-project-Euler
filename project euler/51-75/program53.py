import time
t1=t=time.time()
x=[[1],[0]]
count=0
for i in range(100):
    ##print(x[0])
    x[1]=[0]
    x[1]+=x[0]
    x[0]+=[0]
    for j in range(i+2):
        x[0][j]+=x[1][j]
        if x[0][j]>=1000000:
            count+=1
print(count)
print(time.time()-t)
