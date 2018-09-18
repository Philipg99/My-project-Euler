n = 1000
m = 1
reach = 2000000
diff = 2000000

def cal(n,m):
    return n*m*(n+1)*(m+1)/4

while n>=m:
    t=cal(n,m)
    if abs(reach-t)<diff:
        diff=abs(reach-t)
        val=[n,m,diff]
    if t-reach<0:
        m+=1
    else:
        n-=1

print(val)

