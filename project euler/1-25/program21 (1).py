def d(n):
    i=2
    total =1
    while i*i<n:
        if n%i==0:
            total+=i+n/i
        i+=1
    return total

lst=[]
for i in range(2,10000):
    
    if d(d(i))==i and d(i)>i:
        lst+=[i,d(i)]

print (sum(lst))
        
    
