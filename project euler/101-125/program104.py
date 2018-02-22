import time
t=time.time()
chec=[1,2,3,4,5,6,7,8,9]

fn=1
fn1=1
n=1
while len(str(fn))<9:
    fn,fn1=fn1,fn+fn1
    n+=1



def check(n): 
    f10=n%1000000000
    f10=list(map(int,list(str(f10))))
    f10.sort()
    if f10==chec :
        l10=n//(10**(len(str(n))-9))
        l10=list(map(int,list(str(l10))))
        l10.sort()
        if l10==chec:
            return True
    return False
print(check(123456789))
while True:
    fn,fn1=fn1,fn+fn1
    n+=1
    if check(fn):
       break
    if n%10000==0:
        print(n,time.time()-t)
print(n)
print (time.time()-t)
