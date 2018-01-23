def trans(n):
    n=list(str(n))
    n=list(map(int,n))
    n=list(map(lambda x:x*x,n))
    return sum(n)
count=0
tab=[0]
for i in range(1,568):
    n=i
    while True:
        if n==1:
            tab+=[0]
            break
        if n==89:
            tab+=[1]
            break
        n=trans(n)
for i in range(1,10000000):
    if i%10000==0:
        print(i)
    if tab[trans(i)]==1:
        count+=1
print (count)
        
