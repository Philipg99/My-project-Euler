from string import ascii_uppercase
import time
t=time.time()

fhand=open('prb22.txt','r')
n=fhand.read()
r=n.split()
r.sort()
d = {c : i for i, c in enumerate(ascii_uppercase, 1)}
pos=1
total=0
for name in r:
    prod=0
    for letter in name:
        prod+=d[letter]
    total+=prod*pos
    pos+=1
print(total)
        
print (time.time()-t)
