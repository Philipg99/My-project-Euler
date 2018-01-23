import time
import math
t = time.time()
fhand = open('prb99.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    temp=list(map(int,n.split()))
    r.append(temp)
mx=0
mi=0
for i in range(len(r)):
    r[i][1]*=math.log(r[i][0])
    if r[i][1]>mx:
        mx=r[i][1]
        mi=i

print(mx,mi+1)
print(time.time()-t)
