lar=1
i=2
num=600851475143
while True:
    if i>num:
        break
    while num%i==0:
        num/=i
        lar=i
    i+=1

print(lar)
    
