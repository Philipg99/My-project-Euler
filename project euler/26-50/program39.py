
x=1000
res={}
a=1
b=0
c2=0
while a<=x:
    while a+b+c2<1000:
        c2= (a**2+b**2)**0.5
        c1=int (c2)
        if c2==c1:
            if a+b+c2<1000:
                res[a+b+c2] = res.get(a+b+c2, 0) + 1
        b+=1
    a+=1
    b=0
    c2=0
mv=0
mk=0
for k in res:
    if res[k]>mv:
        mv=res[k]
        mk=k
print(mk,mv)
