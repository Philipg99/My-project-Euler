x=  input ('max of a')
x=int (x)
res=[[0,0,0]]
a=1
b=0
c=0
while a<=x:
    while (a**2+b**2)>=(b+1)**2:
        c= a**2+b**2
        c=int (c**0.5)
        if (a**2+b**2)==(c**2):
            if a+b+c==1000:
                print (a*b*c)
                res+=[[a,b,c]]
        b+=1
    a+=1
    b=0
print (res)
x =input()
