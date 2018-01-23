def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f


count=0
for i in range(10,2540160):
    st=list(map(int,list(str(i))))
    st=list(map(fact,st))
    st=sum(st)
    if i%1000==0:
        print (i)
    if st==i:
        print(st)
        count+=st
print (count)
