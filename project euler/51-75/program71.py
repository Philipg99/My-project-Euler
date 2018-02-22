import time
t=time.time()

n=10**6
diff=10**6
while n>1:
    nu=int(n*3/7)
    fra=nu/n
    
    if fra==3/7:
        nu-=1
        fra=nu/n
        
    if 3/7-fra<diff:
        print(nu,n)
        diff=3/7-fra
    n-=1

print(time.time()-t)
