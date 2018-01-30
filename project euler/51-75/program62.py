import time
t1=time.time()
def dig(n):
    n=list(str(n))
    n.sort()
    n=str(n)
    return n

count={}
n=1
t=True
while t:
    if n%1000==0:
        print(n,time.time()-t1)
    cn=n**3
    cn=dig(cn)
    count[cn] = count.get(cn, n*10) + 1
    n+=1
    if count[cn]%10 ==5:
        print ((count[cn]//10)**3)
        t=False
print (time.time()-t1)
