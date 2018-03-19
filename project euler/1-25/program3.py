i=2
num=600851475143
while num>1:
    while num%i==0:
        num/=i
    if num==1:
        print(i)
        break
    i+=1


