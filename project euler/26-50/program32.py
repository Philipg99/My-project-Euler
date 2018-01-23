import time
t=time.time()

def sumdigit(s):
    f=[False]*10
    for i in range(10):
        f[int(s[i])]=True
    for i in f:
        if i==False:
            return False
    return True

sm=set([])
for i in range(1,10000):
    j=1
    while len(str(i*j)+str(i)+str(j))<=9:
        if len(str(i*j)+str(i)+str(j))==9:
            if sumdigit('0'+str(i*j)+str(i)+str(j)):
                print (i,j,i*j)
                sm|={i*j}
        j+=1
print(sum(sm))
print (time.time()-t)
