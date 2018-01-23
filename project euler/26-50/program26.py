import time
t=time.time()
j=10
l=[]
recm=0
nmax=3
for i in range(4,1000):
        j=10
        l=[]
        while True:
                x=j%i
                if x not in l:
                        l+=[x]
                        j=10*x
                elif (len(l)-l.index(x))>recm:
                        recm=len(l)-l.index(x)
                        nmax=i
                else:
                        break
        
print(nmax,recm,time.time()-t)
