from string import ascii_uppercase
d = {c : i for i, c in enumerate(ascii_uppercase, 1)}
fhand = open('prb42.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    r+=n.split()
s=lambda x: x*(x+1)/2
tri=[s(i) for i in range(1,32)]
count=0
for i in r:
    temp=0
    for j in list(i):
        temp+=d[j]
    if temp in tri:
        count+=1
    temp=0

print (count)
