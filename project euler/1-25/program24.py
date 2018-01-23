def fact(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x


lst=[x for x in range(10)]
lnt=''
per=1000000
for x in range(9,0,-1):
    n=0
    while (n+1)*fact(x)<per:
        n+=1
    lnt+=str(lst.pop(n))
    per-=n*fact(x)
lnt+=str(lst.pop(0))
print(lnt)
