fhand = open('prb89.txt','r')
r=[]
while True:
    n= fhand.readline()
    if n == '':
        break
    r += [n[:-1]]


d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
