import time
t=time.time()

n=2
n1=1
for i in range(2,101):
    f=1
    if i%3==0:
        f=2*(i//3)
    n,n1=n*f+n1,n
f=0
while n>0:
    f+=n%10
    n//=10
    
print(f)
print(time.time()-t)
        
        
