lar=1
i=1
num=600851475143
while True:
    if i>num:
        break
    if num%i==0:
        lar=i
        num/=i #this can be improved easyly
    i+=1

print(lar)
    
