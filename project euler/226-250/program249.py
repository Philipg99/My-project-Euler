import time
t1=t=time.time()
x=[[1],[0]]

for i in range(669+1):
    ##print(x[0])
    x[1]=[0]
    x[1]+=x[0]
    x[0]+=[0]
    for j in range(i+2):
        x[0][j]+=x[1][j]

print((sum(x[0])-1))

print(time.time()-t)
