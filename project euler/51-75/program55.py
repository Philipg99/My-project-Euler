import time
t=time.time()

def rev(n):
    n=str(n)
    n=n[::-1]
    n=int(n)
    return n

def pal(n):
    if n==rev(n):
        return True
    else:
        return False

count=0
for i in range(10000):
    if pal(i) or True:
        lc=1
        n=i
        while lc<51:
            n+=rev(n)
            if pal(n):
                count+=1
                break
            lc+=1
print (10000-count)
    
    
