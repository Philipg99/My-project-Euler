maxn =0
maxc=0
n=2
while n<1000000:
    count =0
    x=n
    while x!=1:
        if x%2==0:
            x/=2
        else:
            x=3*x+1
        count+=1
    if count>maxc:
        maxc=count
        maxn=n
        print (maxn,'  ',maxc)
    n+=1
print (maxn ,'  ',maxc )
## could be improved
