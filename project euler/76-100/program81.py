import time

t = time.time()
fhand = open('prb81.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    temp=list(map(int,n.split()))
    r.append(temp)
a=len(r[0])
for i in range(a-2,-1,-1):
    r[79][i]+=r[a-1][i+1]
    r[i][79]+=r[i+1][a-1]
    

for i in range(a-2,-1,-1):
    for j in range(i,-1,-1):
        if r[i+1][j]<r[i][j+1]:
            r[i][j]+=r[i+1][j]
        else:
            r[i][j]+=r[i][j+1]

        if i!=j:    
            if r[j+1][i]<r[j][i+1]:
                r[j][i]+=r[j+1][i]
            else:
                r[j][i]+=r[j][i+1]

            
print(r[0][0])

print(time.time()-t)
