from itertools import product
import time
tw=time.time()
r4=[]
r6=[]
for i in range(37):
    r4+=[0]
    r6+=[0]

p=[0,0,0,0,0,0,0,0,0,0]
for p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8] in product(range(1,5), repeat =9):
    r4[sum(p)]+=1

for p[0],p[1],p[2],p[3],p[4],p[5] in product(range(1,7), repeat =6):
    r6[sum(p[0:6])]+=1

t=(4**9)*(6**6)
w=0
for c in range(37):
    for p in range(c+1,37):
        w+=r6[c]*r4[p]


print(round(w/t,7))

print(time.time()-tw)
