import time
t= time.time()
def d(n):
    i=2
    total =1
    while i*i<=n:
        if n%i==0 and i*i !=n: ## this mistake to 4hrs to solve
            total+=i+n/i
        if i*i==n:
            total+=i
        i+=1
    return total

abd=[x for x in range(12,28124) if d(x)>x]
y=len(abd)
abd=tuple(abd)
tt=time.time()
sbd=[]
for i in range(y):
    if abd[i]>28124/2:
        break
    for j in range(i,y):
        if abd[i]+abd[j]<28124:
            sbd+=[abd[i]+abd[j]]
        else:
            break
sbd=list(set(sbd))
nn=sum(sbd)
n=28123
total=n*(n+1)/2
total-=nn

print (total)
        
print (time.time()-t)
