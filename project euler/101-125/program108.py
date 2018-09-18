
def y(x,n):
    if n*x%(x-n)==0:
            return 1
    return 0

n=0
while True:
    n+=1 
    c=0
    for x in range(n+1,n*2+1):
        if y(x,n):
            c+=1
    if n%1000==0:
        print(n)
    if c>1000:
        print(n,c)



    
    
