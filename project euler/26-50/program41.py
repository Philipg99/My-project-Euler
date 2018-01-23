def isprime(n):
    x=2
    while x*x<=n:
        if n%x==0:
            return False
        x+=1
    return True

def hasdigit(x):
    x=list(map(int,list(str(x))))
    for i in range(1,8):
        if i not in x:
            return False
    return True

for i in range(7654321,1234567,-1):
    if hasdigit(i):
        if isprime(i):
            print (i)
