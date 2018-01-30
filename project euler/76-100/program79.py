import time
##reading from file
t = time.time()
fhand = open('prb79.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    n=int(n)
    n=list(str(n))
    temp=list(map(int,n))
    r.append(temp)

##

x=[[],[],[],[],[],[],[],[],[],[]]
for c in r:
    if c[1] not in x[c[0]]:
        x[c[0]]+=[c[1]]
    if c[2] not in x[c[0]]:
        x[c[0]]+=[c[2]]
    if c[2] not in x[c[1]]:
        x[c[1]]+=[c[2]]
    for i in range(3):
        if 10 not in x[c[i]]:
            x[c[i]]+=[10]
for i in range(len(x)):
    x[i].sort()
    print(i,x[i])
print(time.time()-t)
