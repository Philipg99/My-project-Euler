import time
t = time.time()
fhand = open('prb67.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    temp=list(map(int,n.split()))
    r.append(temp)
for i in range(len(r)-2,-1,-1):
    for j in range(len(r[i])):

        if r[i+1][j]>r[i+1][j+1]:
            r[i][j]+=r[i+1][j]
        else:
            r[i][j]+=r[i+1][j+1]
print (r[0][0])

print (time.time()-t)
