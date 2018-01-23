

fhand = open('prb13.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    r.append(int(n))
su=sum(r)
while su>10000000000:
    su//=10

print (su)


