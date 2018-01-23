def sumdigit(s):
    f=[False]*10
    for i in range(10):
        f[int(s[i])]=True
    for i in f:
        if i==False:
            return False
    return True


mx=0
mi=0
for i in range(1,10000):
    st=''
    n=1
    while len(st)<9:
        st+=str(i*n)
        n+=1
    if len(st)==9 and sumdigit('0'+st):
        if int(st)>mx:
            mx=int(st)
            mi=i
print (mx,mi)
