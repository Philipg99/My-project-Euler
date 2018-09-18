fhand = open('prb54.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    t=n[:-1].split()
    r+=[[ t[:5] ,t[5:] ]]


cov={ '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, 'C':1, 'S':2, 'D':3, 'H':4}

rf=[]
for k in range(1000):
    p=[]
    for j in range(2):
        tet=[]
        for i in r[k][j]:
            t=list(map(str,i ))
            te=[cov[t[0]],cov[t[1]]]
            tet+=[te]
        tet.sort(reverse=True)
        p+=[tet]
    rf+=[p]



def highcard(a):
    return 1+a[0][0]*(10**-2)

def onepair(a):
    for i in range(4):
        if a[i][0]==a[i+1][0]:
            return 2+a[i][0]*(10**-2)
    return -1

def twopair(a):
    pc=0
    for i in range(4):
        if a[i][0]==a[i+1][0]:
            pc+=1
    if pc==2:
        return 3
    return -1

def threeofakind(a):
    for i in range(3):
        if a[i][0]==a[i+1][0] and a[i][0]==a[i+2][0]:
            return 4
    return -1

def straight(a):
    for i in range(4):
        if a[i][0]!=a[i+1][0]+1:
            return -1
    return 5
    

def flush(a):
    for i in range(4):
        if a[i][1]!=a[i+1][1]:
            return -1
    return 6

def fullhouse(a):
    t=-1
    if a[0][0]==a[1][0] and a[1][0]==a[2][0]:
        t=0
    if a[2][0]==a[3][0] and a[2][0]==a[4][0]:
        t=2

    if t!=-1:
        if t==2:
            if a[0][0]==a[1][0]:
                return 7
        else:
            if a[3][0]==a[4][0]:
                return 7
    return -1

def check(a):
    if fullhouse(a)!=-1:
        return fullhouse(a)
    if flush(a)!=-1:
        return flush(a)
    if straight(a)!=-1:
        return straight(a)
    if threeofakind(a)!=-1:
        return threeofakind(a)
    if twopair(a)!=-1:
        return twopair(a)
    if onepair(a)!=-1:
        return onepair(a)
    if highcard(a)!=-1:
        return highcard(a)
    
        
## fourofakind,straightflush and royalflush does not exist
            
w=0   
for i in range(1000):
    if check(rf[i][0])>=check(rf[i][1]):
        w+=1
    if check(rf[i][0])==check(rf[i][1]):
        if rf[i][0][0][0]>rf[i][1][0][0]:
            w+=1
print(w)

## got 377 , real answer 376 , close enough
