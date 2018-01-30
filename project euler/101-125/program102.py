import time
t=time.time()

fhand = open('prb102.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n=='':
        break
    temp=list(map(int,n.split()))
    r.append(temp)

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
                + x3 * (y1 - y2)) / 2.0)
 

def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area (x1, y1, x2, y2, x3, y3)
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    if(A == A1 + A2 + A3):
        return True
    else:
        return False
 
count=0
for i in r:
    if (isInside(i[0], i[1], i[2], i[3], i[4], i[5], 0, 0)):
        count+=1

print(count)
print(time.time()-t)
