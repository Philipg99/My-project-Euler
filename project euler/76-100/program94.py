

a=2
bl=1
bh=3
s=0
while 2*a+bl<1000000000:
    bl2=bl*bl
    bh2=bh*bh
    a2=a*a
    if a%100000==0:
        print(2*a+bl)
    h1=(a2-bl2/4)**0.5
    h2=(a2-bh2/4)**0.5
    if abs(int(h1*bl/2)-h1*bl/2)<0.0001:
        s+=2*a+bl
        print(h1*bl/2,a,bl)
    if abs(int(h1*bh/2)-h2*bh/2)<0.0001:
        s+=2*a+bh
        print(h1*bl/2,a,bh)
    a+=1
    bh=a+1
    bl=a-1
    
print(s)
    
