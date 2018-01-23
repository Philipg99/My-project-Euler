from itertools import product
import time
t1 = time.time()
fhand = open('prb18.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    temp=list(map(int,n.split()))
    r.append(temp)
maxi=0
             
for i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14  in product(range(2), repeat=14):
    lst=[0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,]
    temp=0
   
    for i in range(15):
        temp+=r[i][sum(lst[0:i+1])]
        
     
    if temp>maxi:
        maxi=temp
print (maxi)
    
print (time.time()-t1)
