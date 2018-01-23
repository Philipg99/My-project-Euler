a=9
b=9
c=9
flag=0
num=1000000 #this is just for the loop to start
while num>100000:
    temp=[c,b,a,a,b,c]
    num=sum( [temp[i]*(10**i) for i in range(6)] )
    if a==0:
        if b==0:
            c-=1
            a=9
            b=9
        else:
            b-=1
            a=9
    else:
        a-=1
        
    test=999
    while test>99:
        if num%test==0 and num/test<1000:
            print (num)
            flag=1
            break
        test-=1
    if flag==1:
        break

