import time
t1=time.time()

def imp(n):
    m=list(str(n))
    m.sort()
    return m

p=0
t=True
while t :
    p+=1
    n=10**(p-1)
    while n<(10**p)/6 and t:
        fp=imp(n)
        flg=0
        for i in range(2,7):
            ch=imp(i*n)
            for j in range(len(fp)):
                if fp[j]!=ch[j]:
                    flg=1
                    break
        n+=1
        if flg==0:
            t=False
                
print(n-1)

print(time.time()-t1)

