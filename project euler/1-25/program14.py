from time import time as t
w=t()

maxn =0
maxc=0
n=2
memo=[0,0]
ml=2
while n<1000000:
    count =0
    x=n
    while x!=1:
        if x<ml:
            count+=memo[x]
            break
        if x%2==0:
            x//=2
        else:
            x=3*x+1
        count+=1
    memo+=[count]
    ml+=1
    if count>maxc:
        maxc=count
        maxn=n
    n+=1
print (maxn ,'  ',maxc )



print(t()-w)
