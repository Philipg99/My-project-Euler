
##copyed from probrlm 127
n=100000
l=[]
for i in range(n+1):
    l+=[[1,i]]


for i in range(2,n+1):
    if l[i][0]==1:
        for j in range(i,n+1,i):
            l[j][0]*=i



