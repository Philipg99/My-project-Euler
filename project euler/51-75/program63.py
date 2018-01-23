count=0
for i in range(1,10):
    n=1
    while len(str(i**n))==n:
        count+=1
        n+=1
print(count)
